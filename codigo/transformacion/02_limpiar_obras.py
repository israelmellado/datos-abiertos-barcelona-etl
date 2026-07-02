from pathlib import Path
import pandas as pd

# =========================
# RUTAS
# =========================
RAIZ = Path(__file__).resolve().parents[2]

ARCHIVO_ENTRADA = RAIZ / "datos" / "crudos" / "obres_espai_public.csv"
ARCHIVO_SALIDA = RAIZ / "datos" / "procesados" / "obres_limpias.csv"


def main():

    print("=" * 60)
    print("LIMPIEZA DE DATOS - OBRAS PÚBLICAS")
    print("=" * 60)

    # =========================
    # CARGA
    # =========================
    df = pd.read_csv(ARCHIVO_ENTRADA)

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
    df["nom_barri"] = df["nom_barri"].fillna("Desconocido")
    df["titol"] = df["titol"].fillna("Sin título")
    df["constructor"] = df["constructor"].fillna("No informado")

    # =========================
    # SELECCIÓN DE COLUMNAS
    # =========================
    columnas_finales = [
        "codi",
        "nom_districte",
        "nom_barri",
        "tipusobra",
        "pressupost_licitacio",
        "pressupost_adjudicacio",
        "data_inici",
        "data_fi",
        "duracion_dias",
        "estat",
        "titol",
        "constructor",
        "geometria_wgs84"
    ]

    df_limpio = df[columnas_finales]

    # =========================
    # GUARDAR RESULTADO
    # =========================
    ARCHIVO_SALIDA.parent.mkdir(parents=True, exist_ok=True)
    df_limpio.to_csv(ARCHIVO_SALIDA, index=False)

    print("\nLimpieza completada ✔")
    print(f"Filas finales: {df_limpio.shape[0]}")
    print(f"Archivo guardado en:\n{ARCHIVO_SALIDA}")


if __name__ == "__main__":
    main()