from agents.pm_agent import pm_agent
from agents.backend_agent import backend_agent
from agents.tools import filesystem

import openai
import json
from config.settings import OPENAI_API_KEY, MODEL_NAME

from autogen import UserProxyAgent

# Crear cliente de OpenAI moderno
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Definir herramientas
functions = [
    {
        "name": "create_file",
        "description": "Crea un archivo de texto en la computadora",
        "parameters": {
            "type": "object",
            "properties": {
                "filepath": {"type": "string", "description": "Ruta del archivo incluyendo nombre"},
                "content": {"type": "string", "description": "Contenido que tendrá el archivo"},
            },
            "required": ["filepath", "content"],
        },
    },
    {
        "name": "create_folder",
        "description": "Crea una carpeta nueva en la computadora",
        "parameters": {
            "type": "object",
            "properties": {
                "folderpath": {"type": "string", "description": "Ruta de la carpeta"},
            },
            "required": ["folderpath"],
        },
    },
    {
        "name": "move_file",
        "description": "Mueve un archivo de un lugar a otro",
        "parameters": {
            "type": "object",
            "properties": {
                "source": {"type": "string", "description": "Ruta del archivo origen"},
                "destination": {"type": "string", "description": "Ruta del archivo destino"},
            },
            "required": ["source", "destination"],
        },
    },
]

tools = {
    "create_file": filesystem.create_file,
    "create_folder": filesystem.create_folder,
    "move_file": filesystem.move_file,
}

user_proxy = UserProxyAgent(
    name="Aldo",
    code_execution_config={
        "work_dir": "projects/project-a",
        "use_docker": False
    },
    max_consecutive_auto_reply=2
)

pm_agent.max_consecutive_auto_reply = 2
backend_agent.max_consecutive_auto_reply = 2

def main():
    # Mensaje inicial
    messages = [
        {"role": "system", "content": """
Eres un desarrollador backend operativo. Tu tarea es analizar los requerimientos
y decidir qué función usar de las disponibles. No escribas texto normal si puedes usar una función.
"""}
    ]

    messages.append({"role": "user", "content": """
Crea la carpeta 'projects/project-a/backend/', crea 'main.py' dentro de ella con código print("Hola desde Backend"),
y mueve el README.md que está en 'projects/project-a/' a 'projects/project-a/backend/'.
"""})

    # Nuevo llamado con el cliente moderno
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        tools=[
            {
                "type": "function",
                "function": func
            } for func in functions
        ],
        tool_choice="auto"
    )

    # Interpretar respuesta
    message = response.choices[0].message

    if message.tool_calls:
        for tool_call in message.tool_calls:
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            if function_name in tools:
                result = tools[function_name](**arguments)
                print(result)
            else:
                print(f"Función {function_name} no disponible.")
    else:
        print("No se requirió llamar función.")

if __name__ == "__main__":
    main()
