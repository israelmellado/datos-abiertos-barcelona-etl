from pathlib import Path
import pandas as pd

# =========================
# RUTAS
# =========================
RAIZ = Path(__file__).resolve().parents[2]
ARCHIVO = RAIZ / "datos" / "procesados" / "obres_limpias.csv"


def main():

    print("=" * 60)
    print("ANÁLISIS DE OBRAS PÚBLICAS - BARCELONA")
    print("=" * 60)

    df = pd.read_csv(ARCHIVO)

    # =========================
    # 1. DISTRITOS
    # =========================
    print("\n📍 OBRAS POR DISTRITO")
    print("-" * 40)
    print(df["nom_districte"].value_counts().head(10))

    # =========================
    # 2. ESTADO DE OBRAS
    # =========================
    print("\n🏗️ ESTADO DE LAS OBRAS")
    print("-" * 40)
    print(df["estat"].value_counts())

    # =========================
    # 3. DURACIÓN MEDIA
    # =========================
    print("\n⏱️ DURACIÓN MEDIA DE LAS OBRAS")
    print("-" * 40)
    print(f"{df['duracion_dias'].mean():.2f} días")

    # =========================
    # 4. TIPOS DE OBRA
    # =========================
    print("\n🧱 TIPOS DE OBRA MÁS FRECUENTES")
    print("-" * 40)
    print(df["tipusobra"].value_counts().head(10))

    # =========================
    # 5. PRESUPUESTO
    # =========================
    print("\n💰 PRESUPUESTO MEDIO")
    print("-" * 40)
    print(f"Licitación: {df['pressupost_licitacio'].mean():.2f}")
    print(f"Adjudicación: {df['pressupost_adjudicacio'].mean():.2f}")


if __name__ == "__main__":
    main()