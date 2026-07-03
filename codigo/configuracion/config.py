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

BASE_DATOS = RAIZ / "base_datos" / "sqlite" / "barcelona.db"

MODELO_SQL = RAIZ / "base_datos" / "modelos" / "modelo_obras.sql"

# ======================================
# CONSULTAS SQL
# ======================================

CONSULTAS_SQL = RAIZ / "base_datos" / "consultas"

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
