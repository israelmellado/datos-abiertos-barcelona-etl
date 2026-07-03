from pathlib import Path
import sys

RAIZ_PROYECTO = Path(__file__).resolve().parents[2]
sys.path.append(str(RAIZ_PROYECTO))

import sqlite3
import pandas as pd

from codigo.configuracion.config import BASE_DATOS, CONSULTAS_SQL
from codigo.utilidades.logger import logger


def main():

    logger.info("Inicio de consultas SQL")

    conexion = sqlite3.connect(BASE_DATOS)

    # =====================================
    # Ejecutar todas las consultas
    # =====================================

    for archivo_sql in sorted(CONSULTAS_SQL.glob("*.sql")):

        print("\n" + "=" * 60)
        print(f"CONSULTA: {archivo_sql.stem}")
        print("=" * 60)

        with open(archivo_sql, "r", encoding="utf-8") as f:
            consulta = f.read()

        resultado = pd.read_sql_query(consulta, conexion)

        print(resultado)

    conexion.close()

    print("\n✔ Todas las consultas ejecutadas correctamente.")
    logger.info("Consultas SQL finalizadas correctamente")


if __name__ == "__main__":
    main()

