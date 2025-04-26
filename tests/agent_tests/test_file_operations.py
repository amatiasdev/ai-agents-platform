from agents.tools.file_system_tools import (
    create_folder,
    create_file,
)

from config.settings import MODEL_NAME, OPENAI_API_KEY
import openai
import json
import os
from schemas.function_schemas import functions_schema

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def test_create_folder_and_file():
    print("🚀 Test: Crear carpeta y archivo usando tools registradas.")

    test_messages = [
        {"role": "system", "content": """
Eres un agente de soporte técnico para Windows. 
Debes usar funciones registradas para crear carpetas o archivos si es necesario.
No expliques. No describas pasos humanos. Ejecuta funciones.
"""}
    ]
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    test_messages.append({
            "role": "user",
            "content": f"""
        Usando las funciones disponibles, crea una carpeta en '{desktop_path}/prueba-carpeta' 
        y dentro crea un archivo llamado 'nota_prueba.txt' con el contenido: 
        'Esta es una nota creada por un agente en pruebas.'
        """
        })

    # Llamamos a OpenAI correctamente
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=test_messages,
        tools=functions_schema,
        tool_choice="auto",
    )

    message = response.choices[0].message

    # Verifica si el modelo invocó funciones
    if hasattr(message, "tool_calls") and message.tool_calls:
        print("\n🔵 Funciones detectadas, ejecutando...")

        for tool_call in message.tool_calls:
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            if function_name == "create_folder":
                print(create_folder(**arguments))
            elif function_name == "create_file":
                print(create_file(**arguments))
            else:
                print(f"⚠️ Función desconocida: {function_name}")
    else:
        print("\n⚠️ El agente no llamó funciones. Resultado textual:")
        print(message.content)

if __name__ == "__main__":
    test_create_folder_and_file()
