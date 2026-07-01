from pathlib import Path
import requests

# URL del recurso CSV
URL = "https://opendata-ajuntament.barcelona.cat/data/dataset/fd9f355f-2160-4f89-96a1-6ece3924e3bd/resource/4e6b3bfe-2f47-4d35-aa7d-3e4bcc930cea/download"

# Ruta del proyecto
proyecto = Path(__file__).resolve().parents[2]

# Carpeta de destino
destino = proyecto / "datos" / "crudos"
destino.mkdir(parents=True, exist_ok=True)

archivo = destino / "obres_espai_public.csv"

print("Descargando datos...")

respuesta = requests.get(URL, timeout=30)
respuesta.raise_for_status()

with open(archivo, "wb") as f:
    f.write(respuesta.content)

print(f"Archivo guardado en:\n{archivo}")