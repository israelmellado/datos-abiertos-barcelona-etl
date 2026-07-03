from pathlib import Path
import sqlite3
import pandas as pd

# =====================================
# Rutas
# =====================================

RAIZ = Path(__file__).resolve().parents[2]

BASE_DATOS = RAIZ / "base_datos" / "sqlite" / "barcelona.db"
CARPETA_SQL = RAIZ / "base_datos" / "consultas"

# =====================================
# Conexión
# =====================================

conexion = sqlite3.connect(BASE_DATOS)

# =====================================
# Ejecutar todas las consultas
# =====================================

for archivo_sql in sorted(CARPETA_SQL.glob("*.sql")):

    print("\n" + "=" * 60)
    print(f"CONSULTA: {archivo_sql.stem}")
    print("=" * 60)

    with open(archivo_sql, "r", encoding="utf-8") as f:
        consulta = f.read()

    resultado = pd.read_sql_query(consulta, conexion)

    print(resultado)

conexion.close()

print("\n✔ Todas las consultas ejecutadas correctamente.")