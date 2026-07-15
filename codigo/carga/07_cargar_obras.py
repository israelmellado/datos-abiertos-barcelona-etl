import sys
from pathlib import Path

RAIZ_PROYECTO = Path(__file__).resolve().parents[2]
sys.path.append(str(RAIZ_PROYECTO))

# import sqlite3
import pandas as pd

from codigo.base_datos.conexion import obtener_conexion
from codigo.configuracion.config import (
    CSV_LIMPIO,
    MOTOR_BD,
)
from codigo.utilidades.logger import logger


def main():
    print(MOTOR_BD)
    logger.info("Inicio de la carga de datos")

    # =====================================
    # Leer CSV
    # =====================================

    df = pd.read_csv(CSV_LIMPIO)

    # =====================================
    # Seleccionar columnas
    # =====================================

    df = df[
        [
            "codi",
            "ubicacio",
            "nom_districte",
            "nom_barri",
            "tipusobra",
            "pressupost_licitacio",
            "pressupost_adjudicacio",
            "data_inici",
            "data_fi",
            "duracion_dias",
            "promotor",
            "constructor",
            "estat",
            "titol",
            "descripcio",
            "url_web_obres",
            "geometria_wgs84",
        ]
    ]

    df.columns = [
        "codigo",
        "ubicacion",
        "distrito",
        "barrio",
        "tipo_obra",
        "presupuesto_licitacion",
        "presupuesto_adjudicacion",
        "fecha_inicio",
        "fecha_fin",
        "duracion_dias",
        "promotor",
        "constructor",
        "estado",
        "titulo",
        "descripcion",
        "url_web_obras",
        "geometria_wgs84",
    ]

    # conexion = sqlite3.connect(BASE_DATOS)
    conexion = obtener_conexion()
    df.to_sql(
        "obras",
        conexion,
        if_exists="append",
        index=False,
    )

    conexion.close()

    print("=" * 50)
    print("DATOS CARGADOS CORRECTAMENTE")
    print("=" * 50)
    print(f"Registros insertados: {len(df)}")

    logger.info(f"Registros insertados: {len(df)}")
    logger.info("Carga de datos finalizada correctamente")


if __name__ == "__main__":
    main()
