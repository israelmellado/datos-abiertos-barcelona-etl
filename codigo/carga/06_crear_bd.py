import sys
from pathlib import Path

RAIZ_PROYECTO = Path(__file__).resolve().parents[2]
sys.path.append(str(RAIZ_PROYECTO))

# import sqlite3

from codigo.base_datos.conexion import obtener_conexion
from codigo.configuracion.config import (
    BASE_DATOS,
    MODELO_SQL,
    MOTOR_BD,
)
from codigo.utilidades.logger import logger


def main():

    logger.info("Creación de la base de datos")

    BASE_DATOS.parent.mkdir(parents=True, exist_ok=True)

    # conexion = sqlite3.connect(BASE_DATOS)
    conexion = obtener_conexion()

    with open(MODELO_SQL, "r", encoding="utf-8") as archivo:
        script_sql = archivo.read()

    if MOTOR_BD == "sqlite":

        cursor = conexion.cursor()
        cursor.executescript(script_sql)
        conexion.commit()
        conexion.close()

    else:
        # PostgreSQL (SQLAlchemy)
        from sqlalchemy import text

        with conexion:
            for sentencia in script_sql.split(";"):
                sentencia = sentencia.strip()
                if sentencia:
                    conexion.execute(text(sentencia))
    print("=" * 50)
    print("BASE DE DATOS CREADA CORRECTAMENTE")
    print("=" * 50)
    print(BASE_DATOS)

    logger.info(f"Base de datos creada: {BASE_DATOS}")
    logger.info("Creación de la base de datos finalizada")


if __name__ == "__main__":
    main()
