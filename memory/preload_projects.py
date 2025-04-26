from memory.memory_manager import save_memory, suggest_tags
import datetime
import random
import time

# Lista de proyectos de prueba
sample_projects = [
    "Desarrollo de API REST para sistema de facturación electrónica.",
    "Automatización de reportes financieros usando Python y Pandas.",
    "Implementación de plataforma de agentes IA para gestión de proyectos.",
    "Optimización de consultas en base de datos MySQL para plataforma web.",
    "Construcción de sistema de notificaciones push para aplicaciones móviles.",
    "Despliegue de microservicios con Kubernetes y Docker.",
    "Integración de chatbot inteligente en plataforma de soporte técnico.",
    "Creación de dashboards de analítica web con Power BI y Google Analytics.",
    "Sistema de detección de anomalías en redes de sensores IoT.",
    "Automatización de backups de servidores en la nube AWS."
]

def preload_projects():
    print("🚀 Cargando proyectos de prueba en memoria...\n")

    for idx, description in enumerate(sample_projects):
        tags = suggest_tags(description)
        project_id = f"sample-project-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(1000,9999)}"

        save_memory(
            project_id=project_id,
            description=description,
            tags=tags
        )

        print(f"✅ Proyecto {idx+1}/10 guardado: {project_id}")
        time.sleep(1)  # Pequeña pausa para asegurar IDs únicos

    print("\n🎉 ¡Carga de proyectos de prueba completada!")

if __name__ == "__main__":
    preload_projects()
