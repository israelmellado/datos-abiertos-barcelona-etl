from pathlib import Path
import sys

RAIZ_PROYECTO = Path(__file__).resolve().parents[2]
sys.path.append(str(RAIZ_PROYECTO))

import requests

from codigo.configuracion.config import CSV_CRUDO
from codigo.utilidades.logger import logger

# URL del recurso CSV
URL = (
    "https://opendata-ajuntament.barcelona.cat/data/dataset/"
    "fd9f355f-2160-4f89-96a1-6ece3924e3bd/resource/"
    "4e6b3bfe-2f47-4d35-aa7d-3e4bcc930cea/download"
)

def main():

    logger.info("Inicio de la descarga de datos")

    # Crear carpeta si no existe
    CSV_CRUDO.parent.mkdir(parents=True, exist_ok=True)

    print("Descargando datos...")

    respuesta = requests.get(URL, timeout=30)
    respuesta.raise_for_status()

    with open(CSV_CRUDO, "wb") as f:
        f.write(respuesta.content)

    print(f"Archivo guardado en:\n{CSV_CRUDO}")

    logger.info(f"Archivo descargado: {CSV_CRUDO}")
    logger.info("Descarga completada correctamente")


if __name__ == "__main__":
    main()