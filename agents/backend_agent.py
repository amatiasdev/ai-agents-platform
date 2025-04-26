from autogen import AssistantAgent
from config.settings import OPENAI_API_KEY, MODEL_NAME

backend_agent = AssistantAgent(
    name="BackendAgent",
    system_message="""
Eres un desarrollador backend experto. Debes recibir especificaciones técnicas,
usar herramientas disponibles como filesystem para crear archivos o carpetas,
y reportar tu progreso de manera profesional.
""",
    llm_config={
        "config_list": [{"model": MODEL_NAME, "api_key": OPENAI_API_KEY}],
        "temperature": 0,
    }
)
