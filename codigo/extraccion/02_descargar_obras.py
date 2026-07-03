import sys
from pathlib import Path

RAIZ_PROYECTO = Path(__file__).resolve().parents[2]
sys.path.append(str(RAIZ_PROYECTO))

import requests

from codigo.configuracion.config import CSV_CRUDO
from codigo.utilidades.logger import logger

URL = (
    "https://opendata-ajuntament.barcelona.cat/data/dataset/"
    "fd9f355f-2160-4f89-96a1-6ece3924e3bd/resource/"
    "4e6b3bfe-2f47-4d35-aa7d-3e4bcc930cea/download"
)


def main():

    logger.info("Inicio de la descarga de datos")

    CSV_CRUDO.parent.mkdir(parents=True, exist_ok=True)

    print("Descargando datos...")

    respuesta = requests.get(
        URL,
        timeout=30,
        allow_redirects=True,
        headers={"User-Agent": "Mozilla/5.0"},
    )
    print("Status:", respuesta.status_code)
    print("Content-Type:", respuesta.headers.get("Content-Type"))
    print("URL final:", respuesta.url)
    print(respuesta.text[:500])

    respuesta.raise_for_status()

    with open(CSV_CRUDO, "wb") as f:
        f.write(respuesta.content)

   # print("Primeros 200 caracteres del archivo:")
   # with open(CSV_CRUDO, "r", encoding="utf-8", errors="ignore") as f:
   #     print(f.read(200))

    print(f"\nArchivo guardado en:\n{CSV_CRUDO}")

    logger.info(f"Archivo descargado: {CSV_CRUDO}")
    logger.info("Descarga completada correctamente")


if __name__ == "__main__":
    main()
