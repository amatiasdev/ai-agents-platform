from autogen import AssistantAgent
from config.settings import OPENAI_API_KEY, MODEL_NAME

pm_agent = AssistantAgent(
    name="PMAgent",
    system_message="""
Eres un Project Manager técnico. Tu tarea es recibir requerimientos del usuario,
analizarlos, dividirlos en tareas claras y asignarlas al BackendAgent de forma organizada y específica.
""",
    llm_config={
        "config_list": [{"model": MODEL_NAME, "api_key": OPENAI_API_KEY}],
        "temperature": 0,
    },
    max_consecutive_auto_reply=2
)
