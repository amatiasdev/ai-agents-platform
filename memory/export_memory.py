import json
import os
import chromadb

def export_memory(output_file="memory_backup.json"):
    """
    Exporta todos los proyectos almacenados en memoria a un archivo JSON.
    """
    chroma_client = chromadb.PersistentClient(path="./memory/chroma_store")
    collection_name = "project_memory"
    collection = chroma_client.get_or_create_collection(collection_name)

    # Obtener todos los documentos e IDs
    results = collection.get()
    documents = results.get('documents', [])
    ids = results.get('ids', [])

    if not documents:
        print("❌ No hay proyectos guardados en memoria para exportar.")
        return

    # Armar estructura de backup
    memory_data = []
    for proj_id, doc in zip(ids, documents):
        memory_data.append({
            "project_id": proj_id,
            "content": doc
        })

    # Guardar en JSON
    output_path = os.path.join(".", "memory", output_file)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(memory_data, f, indent=4, ensure_ascii=False)

    print(f"✅ Memoria exportada exitosamente a {output_path}")

if __name__ == "__main__":
    export_memory()
