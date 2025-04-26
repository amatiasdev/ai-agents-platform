import json
import os
import chromadb

def import_memory(input_file="memory_backup.json"):
    """
    Importa proyectos almacenados en un archivo JSON a la memoria persistente de Chroma.
    """
    input_path = os.path.join(".", "memory", input_file)

    if not os.path.exists(input_path):
        print(f"❌ El archivo {input_file} no existe en la carpeta memory.")
        return

    with open(input_path, "r", encoding="utf-8") as f:
        memory_data = json.load(f)

    if not memory_data:
        print("❌ El archivo de memoria está vacío.")
        return

    chroma_client = chromadb.PersistentClient(path="./memory/chroma_store")
    collection_name = "project_memory"
    collection = chroma_client.get_or_create_collection(collection_name)

    print("🚀 Importando proyectos a la memoria...\n")

    for idx, item in enumerate(memory_data):
        project_id = item.get("project_id")
        content = item.get("content")

        if project_id and content:
            collection.add(
                documents=[content],
                ids=[project_id]
            )
            print(f"✅ Proyecto {idx+1}/{len(memory_data)} importado: {project_id}")
        else:
            print(f"⚠️ Proyecto {idx+1} inválido, omitiendo.")

    print(f"\n🎉 ¡Importación completada! Total: {len(memory_data)} proyectos.")

if __name__ == "__main__":
    import_memory()
