import os
import shutil
import zipfile

def create_folder(path: str) -> str:
    """
    Crea una carpeta en el sistema de archivos.
    """
    try:
        os.makedirs(path, exist_ok=True)
        return f"✅ Carpeta creada exitosamente en: {path}"
    except Exception as e:
        return f"❌ Error al crear carpeta: {str(e)}"

def create_file(path: str, content: str = "") -> str:
    """
    Crea un archivo con contenido opcional.
    """
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"✅ Archivo creado exitosamente en: {path}"
    except Exception as e:
        return f"❌ Error al crear archivo: {str(e)}"

def move_file(src_path: str, dest_path: str) -> str:
    """
    Mueve un archivo o carpeta de un lugar a otro.
    """
    try:
        shutil.move(src_path, dest_path)
        return f"✅ Archivo/carpeta movido de {src_path} a {dest_path}"
    except Exception as e:
        return f"❌ Error al mover archivo/carpeta: {str(e)}"

def copy_file(src_path: str, dest_path: str) -> str:
    """
    Copia un archivo de un lugar a otro.
    """
    try:
        shutil.copy2(src_path, dest_path)
        return f"✅ Archivo copiado de {src_path} a {dest_path}"
    except Exception as e:
        return f"❌ Error al copiar archivo: {str(e)}"

def delete_file_or_folder(path: str) -> str:
    """
    Elimina un archivo o una carpeta.
    """
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
        return f"✅ Archivo/carpeta eliminado: {path}"
    except Exception as e:
        return f"❌ Error al eliminar archivo/carpeta: {str(e)}"

def compress_folder(folder_path: str, zip_path: str) -> str:
    """
    Comprime una carpeta en un archivo .zip.
    """
    try:
        shutil.make_archive(zip_path.replace('.zip', ''), 'zip', folder_path)
        return f"✅ Carpeta comprimida exitosamente en: {zip_path}"
    except Exception as e:
        return f"❌ Error al comprimir carpeta: {str(e)}"

def get_desktop_path() -> str:
    """
    Devuelve la ruta del escritorio del usuario actual en Windows.
    """
    return os.path.join(os.path.expanduser("~"), "Desktop")

