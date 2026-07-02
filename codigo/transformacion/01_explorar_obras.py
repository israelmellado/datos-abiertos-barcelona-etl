from pathlib import Path
import pandas as pd

# Ruta al archivo CSV
RAIZ_PROYECTO = Path(__file__).resolve().parents[2]
ARCHIVO_CSV = RAIZ_PROYECTO / "datos" / "crudos" / "obres_espai_public.csv"

print("=" * 50)
print("ANÁLISIS DEL DATASET: OBRAS PÚBLICAS")
print("=" * 50)

# Leer el CSV
df = pd.read_csv(ARCHIVO_CSV)

# Información general
print(f"\nNúmero de filas: {df.shape[0]}")
print(f"Número de columnas: {df.shape[1]}")

# Columnas
print("\nColumnas:")
for columna in df.columns:
    print(f" - {columna}")

# Tipos de datos
print("\nTipos de datos:")
print(df.dtypes)

# Valores nulos
print("\nValores nulos por columna:")
print(df.isnull().sum())

# Primeras filas
print("\nPrimeras 5 filas:")
print(df.head())