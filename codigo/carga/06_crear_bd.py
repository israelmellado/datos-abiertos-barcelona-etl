from pathlib import Path
import sys

RAIZ_PROYECTO = Path(__file__).resolve().parents[2]
sys.path.append(str(RAIZ_PROYECTO))

import sqlite3

from codigo.configuracion.config import BASE_DATOS, MODELO_SQL
from codigo.utilidades.logger import logger


def main():

    logger.info("Creación de la base de datos")

    BASE_DATOS.parent.mkdir(parents=True, exist_ok=True)

    conexion = sqlite3.connect(BASE_DATOS)
    cursor = conexion.cursor()

    with open(MODELO_SQL, "r", encoding="utf-8") as archivo:
        script_sql = archivo.read()

    cursor.executescript(script_sql)

    conexion.commit()
    conexion.close()

    print("=" * 50)
    print("BASE DE DATOS CREADA CORRECTAMENTE")
    print("=" * 50)
    print(BASE_DATOS)

    logger.info(f"Base de datos creada: {BASE_DATOS}")
    logger.info("Creación de la base de datos finalizada")


if __name__ == "__main__":
    main()