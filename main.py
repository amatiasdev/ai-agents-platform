from agents.pm_agent import pm_agent
from agents.backend_agent import backend_agent
from agents.tools.tool_manager import tool_definitions, execute_tool

import openai
import json
from config.settings import OPENAI_API_KEY, MODEL_NAME
from memory.memory_manager import save_memory, search_memory
from autogen import UserProxyAgent

client = openai.OpenAI(api_key=OPENAI_API_KEY)

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

    print("🚀 Bienvenido al Sistema de Agentes IA")
    query = input("🔎 ¿Quieres buscar proyectos similares antes de empezar? Escribe palabras clave o presiona Enter para omitir: ")

    if query.strip() != "":
        results = search_memory(query)
        if results['documents'][0]:  # Verifica si hay resultados
            print("\n🧠 Proyectos similares encontrados:")
            for idx, doc in enumerate(results['documents'][0]):
                print(f"{idx+1}. {doc}")
            print("\nPuedes considerar estos recuerdos antes de crear el nuevo proyecto.")
        else:
            print("\n❌ No se encontraron recuerdos similares.")
    else:
        print("\n🔹 Continuando sin búsqueda de memoria.")

    # A partir de aquí sigue el flujo normal:
    # (UserProxyAgent → PM Agent → Backend Agent → ejecutar tools)

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

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        tools=tool_definitions,
        tool_choice="auto"
    )

    message = response.choices[0].message

    if message.tool_calls:
        for tool_call in message.tool_calls:
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            result = execute_tool(function_name, arguments)
            print(result)
    else:
        print("No se requirió llamar función.")

    
    # Finalmente guarda el nuevo proyecto en memoria
    save_memory(
        project_id="ai-agents-platform",
        description="Primera versión de plataforma de agentes IA operativos: PM Agent, Backend Agent, creación de carpetas y archivos, memoria persistente en ChromaDB."
    )
    

if __name__ == "__main__":
    main()
