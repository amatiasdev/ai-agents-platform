# function_schemas.py

functions_schema = [
    {
        "type": "function",
        "function": {
            "name": "create_folder",
            "description": "Crea una nueva carpeta en el sistema de archivos.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Ruta completa donde se creará la carpeta."
                    }
                },
                "required": ["path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_file",
            "description": "Crea un archivo de texto con contenido opcional.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Ruta completa donde se creará el archivo."
                    },
                    "content": {
                        "type": "string",
                        "description": "Contenido que tendrá el archivo."
                    }
                },
                "required": ["path", "content"]
            }
        }
    }
]
