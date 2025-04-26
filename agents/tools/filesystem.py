import os
import shutil

def create_file(filepath: str, content: str = ""):
    folder = os.path.dirname(filepath)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Archivo '{filepath}' creado exitosamente."

def create_folder(folderpath: str):
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
        return f"Carpeta '{folderpath}' creada exitosamente."
    else:
        return f"La carpeta '{folderpath}' ya existe."

def move_file(source: str, destination: str):
    if not os.path.exists(source):
        return f"Error: el archivo origen '{source}' no existe."
    destination_folder = os.path.dirname(destination)
    if destination_folder and not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    shutil.move(source, destination)
    return f"Archivo movido de '{source}' a '{destination}'."
