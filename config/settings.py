from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# API KEY de OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configuración de modelo
MODEL_NAME = "gpt-4-1106-preview"  # O "gpt-4" o "gpt-3.5-turbo-1106"
