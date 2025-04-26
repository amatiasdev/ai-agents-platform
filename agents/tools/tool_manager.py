import json
from . import filesystem

# Mapeo de funciones reales
tools = {
    "create_file": filesystem.create_file,
    "create_folder": filesystem.create_folder,
    "move_file": filesystem.move_file,
}

# Definiciones de herramientas para function calling (OpenAI / LangChain)
tool_definitions = [
    {
        "type": "function",
        "function": {
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
    },
    {
        "type": "function",
        "function": {
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
    },
    {
        "type": "function",
        "function": {
            "name": "move_file",
            "description": "Mueve un archivo de un lugar a otro en la computadora",
            "parameters": {
                "type": "object",
                "properties": {
                    "source": {"type": "string", "description": "Ruta del archivo origen"},
                    "destination": {"type": "string", "description": "Ruta del archivo destino"},
                },
                "required": ["source", "destination"],
            },
        },
    },
]

# Función auxiliar para obtener tool real
def execute_tool(function_name: str, arguments: dict):
    if function_name in tools:
        return tools[function_name](**arguments)
    else:
        return f"Función {function_name} no disponible."
