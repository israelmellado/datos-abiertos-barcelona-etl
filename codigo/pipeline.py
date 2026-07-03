from pathlib import Path
import subprocess
import sys

from codigo.utilidades.logger import logger

RAIZ = Path(__file__).resolve().parent

scripts = [
     ("Descarga de datos", "extraccion/02_descargar_obras.py"),
     ("Limpieza", "transformacion/02_limpiar_obras.py"),
     ("Crear base de datos", "carga/06_crear_bd.py"),
     ("Carga de datos", "carga/07_cargar_obras.py"),
     ("Consultas SQL", "carga/08_consultas_sql.py"),
     ("Dashboard", "visualizacion/05_dashboard_obras.py"),
]

print("=" * 60)
print("PIPELINE ETL BARCELONA OPEN DATA")
print("=" * 60)

logger.info("Inicio del pipeline")

for nombre, script in scripts:

    print(f"\n▶ {nombre}")
    logger.info(nombre)

    ruta = RAIZ / script

    if not ruta.exists():
        print(f"❌ No existe: {ruta}")
        logger.error(f"No existe el script: {ruta}")
        break

    print(f"\n▶ Ejecutando: {script}")
    logger.info(f"Ejecutando: {script}")

    resultado = subprocess.run([sys.executable, str(ruta)])
    
    if resultado.returncode == 0:
        logger.info(f"Finalizado correctamente: {script}")
        print("✔ Finalizado")

    if resultado.returncode != 0:
        print(f"\n❌ Error en: {script}")
        logger.error(f"Error ejecutando: {script}")
        break

print("\n" + "=" * 60)
print("PIPELINE FINALIZADO CORRECTAMENTE")
print("=" * 60)
logger.info("Pipeline finalizado")