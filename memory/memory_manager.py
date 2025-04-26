import chromadb
from chromadb.config import Settings

# Inicializar cliente de Chroma
chroma_client = chromadb.Client(
    Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory="./memory/chroma_store"
    )
)

# Crear o cargar colección
collection_name = "project_memory"
collection = chroma_client.get_or_create_collection(collection_name)

def save_memory(project_id: str, description: str):
    """
    Guarda un recuerdo asociado a un proyecto.
    """
    collection.add(
        documents=[description],
        ids=[project_id]
    )
    chroma_client.persist()
    print(f"🧠 Memoria guardada para el proyecto '{project_id}'.")

def search_memory(query: str, n_results: int = 3):
    """
    Busca recuerdos similares a la consulta dada.
    """
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return results
