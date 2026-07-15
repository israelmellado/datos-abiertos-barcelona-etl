from pathlib import Path

# ======================================
# RAÍZ DEL PROYECTO
# ======================================

RAIZ = Path(__file__).resolve().parents[2]

# ======================================
# DATOS
# ======================================

DATOS = RAIZ / "datos"

CSV_CRUDO = DATOS / "crudos" / "obres_espai_public.csv"
CSV_LIMPIO = DATOS / "procesados" / "obres_limpias.csv"

# ======================================
# BASE DE DATOS
# ======================================
MOTOR_BD = "sqlite"
MOTOR_BD = "postgres"
BASE_DATOS = RAIZ / "base_datos" / "sqlite" / "barcelona.db"

MODELO_SQLITE = RAIZ / "base_datos" / "modelos" / "modelo_sqlite.sql"
MODELO_POSTGRES = RAIZ / "base_datos" / "modelos" / "modelo_postgres.sql"

if MOTOR_BD == "sqlite":
    MODELO_SQL = MODELO_SQLITE
elif MOTOR_BD == "postgres":
    MODELO_SQL = MODELO_POSTGRES
else:
    raise ValueError(f"Motor no soportado: {MOTOR_BD}")


# if MOTOR_BD == "sqlite":
#  CONSULTAS_SQL = RAIZ / "base_datos" / "consultas_sqlite"
# else:
#   CONSULTAS_SQL = RAIZ / "base_datos" / "consultas_postgres"
# ======================================
# CONSULTAS SQL
# ======================================

CONSULTAS_SQLITE = RAIZ / "base_datos" / "consultas_sqlite"

CONSULTAS_POSTGRES = RAIZ / "base_datos" / "consultas_postgres"

CONSULTAS_BI = RAIZ / "base_datos" / "consultas_bi"


if MOTOR_BD == "sqlite":
    CONSULTAS_SQL = CONSULTAS_SQLITE

elif MOTOR_BD == "postgres":
    CONSULTAS_SQL = CONSULTAS_POSTGRES

else:
    raise ValueError(f"Motor no soportado: {MOTOR_BD}")

# ======================================
# DOCUMENTACIÓN
# ======================================

IMAGENES = RAIZ / "documentacion" / "imagenes"

# ======================================
# LOGS
# ======================================

LOGS = RAIZ / "logs"
ARCHIVO_LOG = LOGS / "pipeline.log"

# ======================================
# CONSTANTES
# ======================================

PIPELINE_SCRIPTS = [
    ("Descarga de datos", "extraccion/02_descargar_obras.py"),
    ("Limpieza", "transformacion/02_limpiar_obras.py"),
    ("Crear base de datos", "carga/06_crear_bd.py"),
    ("Carga de datos", "carga/07_cargar_obras.py"),
    ("Consultas SQL", "carga/08_consultas_sql.py"),
    ("Dashboard", "visualizacion/05_dashboard_obras.py"),
]

# ======================================
# PostgreSQL
# ======================================

HOST = "localhost"
PUERTO = 5432
USUARIO = "postgres"
PASSWORD = "coloso01"
BASE_DATOS_POSTGRES = "barcelona_etl"
