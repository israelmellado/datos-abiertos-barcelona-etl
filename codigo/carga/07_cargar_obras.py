from pathlib import Path
import sqlite3
import pandas as pd

# =====================================
# Rutas
# =====================================

RAIZ_PROYECTO = Path(__file__).resolve().parents[2]

BASE_DATOS = RAIZ_PROYECTO / "base_datos" / "sqlite" / "barcelona.db"

CSV = RAIZ_PROYECTO / "datos" / "procesados" / "obres_limpias.csv"

# =====================================
# Leer CSV
# =====================================

df = pd.read_csv(CSV)

# =====================================
# Seleccionar columnas del modelo
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

# Renombrar columnas para adaptarlas al modelo SQL

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

# =====================================
# Conexión SQLite
# =====================================

conexion = sqlite3.connect(BASE_DATOS)

# Insertar datos

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