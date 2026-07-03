from pathlib import Path
import sqlite3

# ==========================
# Rutas del proyecto
# ==========================

RAIZ_PROYECTO = Path(__file__).resolve().parents[2]

BASE_DATOS = RAIZ_PROYECTO / "base_datos" / "sqlite" / "barcelona.db"

MODELO_SQL = RAIZ_PROYECTO / "base_datos" / "modelos" / "modelo_obras.sql"

# ==========================
# Crear la base de datos
# ==========================

conexion = sqlite3.connect(BASE_DATOS)

cursor = conexion.cursor()

# Leer el modelo SQL

with open(MODELO_SQL, "r", encoding="utf-8") as archivo:
    script_sql = archivo.read()

cursor.executescript(script_sql)

conexion.commit()
conexion.close()

print("=" * 50)
print("BASE DE DATOS CREADA CORRECTAMENTE")
print("=" * 50)
print(BASE_DATOS)