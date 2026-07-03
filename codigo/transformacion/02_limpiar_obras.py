from pathlib import Path
import sys


RAIZ_PROYECTO = Path(__file__).resolve().parents[2]
sys.path.append(str(RAIZ_PROYECTO))

import pandas as pd

from codigo.configuracion.config import CSV_CRUDO, CSV_LIMPIO
from codigo.utilidades.logger import logger



def main():

    logger.info("Inicio de la limpieza de datos")
    

    # =========================
    # CARGA
    # =========================
    df = pd.read_csv(CSV_CRUDO)

    logger.info(f"Filas iniciales: {df.shape[0]}")
    logger.info(f"Columnas iniciales: {df.shape[1]}")
                
    print(f"\nFilas iniciales: {df.shape[0]}")
    print(f"Columnas iniciales: {df.shape[1]}")

    # =========================
    # CONVERTIR FECHAS
    # =========================
    df["data_inici"] = pd.to_datetime(df["data_inici"], errors="coerce")
    df["data_fi"] = pd.to_datetime(df["data_fi"], errors="coerce")

    # =========================
    # CREAR VARIABLE NUEVA
    # =========================
    df["duracion_dias"] = (df["data_fi"] - df["data_inici"]).dt.days

    # =========================
    # TRATAMIENTO DE NULOS
    # =========================
    df["promotor"] = df["promotor"].fillna("No informado")
    df["descripcio"] = df["descripcio"].fillna("")
    df["ubicacio"] = df["ubicacio"].fillna("")
    df["url_web_obres"] = df["url_web_obres"].fillna("")

    # =========================
    # ELIMINAR DUPLICADOS
    # =========================

    filas_antes = len(df)

    df = df.drop_duplicates(subset="codi", keep="first")

    filas_despues = len(df)

    print(f"Duplicados eliminados: {filas_antes - filas_despues}")
    logger.info(f"Duplicados eliminados: {filas_antes - filas_despues}")
    # =========================
    # SELECCIÓN DE COLUMNAS
    # =========================
    columnas_finales = [
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

    df_limpio = df[columnas_finales]

    # =========================
    # GUARDAR RESULTADO
    # =========================
    CSV_LIMPIO.parent.mkdir(parents=True, exist_ok=True)
    df_limpio.to_csv(CSV_LIMPIO, index=False)

    print("\nLimpieza completada ✔")
    print(f"Filas finales: {df_limpio.shape[0]}")
   
    logger.info(f"Filas finales: {df_limpio.shape[0]}")
    logger.info(f"Archivo generado: {CSV_LIMPIO}")
    logger.info("Limpieza completada correctamente")

if __name__ == "__main__":
    main()