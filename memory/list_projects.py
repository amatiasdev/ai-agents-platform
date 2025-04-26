from memory.memory_manager import search_memory
import chromadb

def list_projects():
    """
    Lista todos los proyectos almacenados en memoria.
    """
    chroma_client = chromadb.PersistentClient(path="./memory/chroma_store")
    collection_name = "project_memory"
    collection = chroma_client.get_or_create_collection(collection_name)

    # Obtener todos los documentos almacenados
    results = collection.get()

    documents = results.get('documents', [])
    ids = results.get('ids', [])

    if not documents:
        print("❌ No hay proyectos guardados en memoria.")
        return

    print("\n🧠 Proyectos en Memoria:\n")

    for idx, (doc, proj_id) in enumerate(zip(documents, ids)):
        first_line = doc.strip().split('\n')[0]
        print(f"{idx+1}. {proj_id} - {first_line}")

    print(f"\n📦 Total de proyectos encontrados: {len(documents)}")

if __name__ == "__main__":
    list_projects()
