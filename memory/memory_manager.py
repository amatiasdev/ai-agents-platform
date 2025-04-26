import datetime
import chromadb
import openai
from config.settings import OPENAI_API_KEY, MODEL_NAME

# Crear cliente OpenAI
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Inicializar cliente de Chroma
chroma_client = chromadb.PersistentClient(path="./memory/chroma_store")

collection_name = "project_memory"
collection = chroma_client.get_or_create_collection(collection_name)

def save_memory(project_id: str, description: str, tags: list = []):
    """
    Guarda un recuerdo de proyecto con tags opcionales.
    """
    full_description = description
    if tags:
        tags_text = ", ".join(tags)
        full_description += f"\nTags: {tags_text}"

    collection.add(
        documents=[full_description],
        ids=[project_id]
    )
    print(f"🧠 Memoria guardada para el proyecto '{project_id}' con tags: {tags}")

def search_memory(query: str, n_results: int = 3):
    """
    Busca recuerdos similares a la consulta dada.
    """
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return results

def suggest_tags(description: str, n_tags: int = 5):
    """
    Usa OpenAI para sugerir automáticamente tags relevantes para una descripción.
    """
    prompt = f"""
Analiza el siguiente resumen de un proyecto y sugiere {n_tags} palabras clave (tags) relevantes, separadas solo por comas.

Resumen:
\"\"\"
{description}
\"\"\"

Devuelve únicamente la lista de palabras separadas por comas, sin numerarlas ni explicar.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )

    tags_text = response.choices[0].message.content.strip()
    tags = [tag.strip() for tag in tags_text.split(",") if tag.strip()]
    return tags

def save_memory(project_id: str, description: str, tags: list = []):
    """
    Guarda un recuerdo de proyecto con tags opcionales y fecha/hora.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    full_description = f"""
Descripción:
{description}

Tags:
{", ".join(tags) if tags else "sin tags"}

Fecha de creación:
{timestamp}
"""

    collection.add(
        documents=[full_description],
        ids=[project_id]
    )
    print(f"🧠 Memoria guardada para el proyecto '{project_id}' con tags: {tags} en {timestamp}")
