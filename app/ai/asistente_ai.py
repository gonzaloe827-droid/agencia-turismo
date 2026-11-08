
import os
from groq import Groq
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Configuracion de Groq
API_KEY = os.getenv("AI_API_KEY")
MODEL = os.getenv("AI_MODEL")

if not API_KEY:
    raise ValueError("No se encontro AI_API_KEY en el archivo .env")

cliente_groq = Groq(api_key=API_KEY)


def consultar_ia(pregunta, informacion_agencia):
    """
    Envia una pregunta a Groq utilizando
    la informacion real de la agencia.
    """

    instrucciones = """
    Eres un asistente turistico de una agencia
    de turismo ubicada en Uyuni, Bolivia.

    Tu trabajo es informar sobre los paquetes
    turisticos y sus itinerarios.

    REGLAS:
    1. Utiliza solamente la informacion proporcionada.
    2. No inventes precios, actividades ni duraciones.
    3. Si no encuentras la respuesta, indica que
       no tienes esa informacion registrada.
    4. Responde en español de forma amable y clara.
    5. Recomienda paquetes solamente cuando los
       datos disponibles permitan hacerlo.
    """

    try:
        respuesta = cliente_groq.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": instrucciones
                },
                {
                    "role": "user",
                    "content": (
                        "INFORMACION DE LA AGENCIA:\n"
                        + informacion_agencia
                        + "\n\nPREGUNTA DEL CLIENTE:\n"
                        + pregunta
                    )
                }
            ],
            temperature=0.3
        )

        return respuesta.choices[0].message.content

    except Exception as error:
        print("Error al consultar Groq:", error)
        return (
            "Lo siento, no pude obtener una respuesta "
            "en este momento. Intenta nuevamente."
        )
