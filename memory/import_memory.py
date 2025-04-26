import json
import os
import chromadb

def import_memory(input_file="memory_backup.json"):
    """
    Importa proyectos desde un archivo JSON a la memoria persistente de Chroma, evitando duplicados.
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

    # Obtener todos los IDs ya existentes
    existing = collection.get()
    existing_ids = set(existing.get('ids', []))

    print("🚀 Importando proyectos a la memoria...\n")

    imported = 0
    skipped = 0

    for idx, item in enumerate(memory_data):
        project_id = item.get("project_id")
        content = item.get("content")

        if not project_id or not content:
            print(f"⚠️ Proyecto {idx+1} inválido, omitiendo.")
            skipped += 1
            continue

        if project_id in existing_ids:
            print(f"⚠️ Proyecto ya existente: {project_id} - Omitido.")
            skipped += 1
        else:
            collection.add(
                documents=[content],
                ids=[project_id]
            )
            print(f"✅ Proyecto {idx+1}/{len(memory_data)} importado: {project_id}")
            imported += 1

    print(f"\n🎉 Importación completada: {imported} proyectos importados, {skipped} proyectos omitidos.")

if __name__ == "__main__":
    import_memory()
