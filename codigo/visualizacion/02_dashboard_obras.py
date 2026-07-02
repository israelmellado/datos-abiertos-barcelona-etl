from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# RUTAS
# =========================
RAIZ = Path(__file__).resolve().parents[2]
ARCHIVO = RAIZ / "datos" / "procesados" / "obres_limpias.csv"
SALIDA = RAIZ / "documentacion" / "imagenes"

SALIDA.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(ARCHIVO)

# =========================
# FUNCIONES AUXILIARES
# =========================
def guardar(figura, nombre):
    ruta = SALIDA / nombre
    figura.savefig(ruta, bbox_inches="tight", dpi=150)
    print(f"Guardado: {ruta}")

# =========================
# 1. OBRAS POR DISTRITO
# =========================
fig, ax = plt.subplots(figsize=(10, 5))
df["nom_districte"].value_counts().head(10).plot(kind="bar", ax=ax)
ax.set_title("Obras por distrito (Top 10)")
ax.set_xlabel("Distrito")
ax.set_ylabel("Número de obras")
plt.xticks(rotation=45)
guardar(fig, "01_obras_por_distrito.png")
plt.close()

# =========================
# 2. ESTADO DE OBRAS
# =========================
fig, ax = plt.subplots(figsize=(6, 5))
df["estat"].value_counts().plot(kind="bar", ax=ax)
ax.set_title("Estado de las obras")
ax.set_xlabel("Estado")
ax.set_ylabel("Cantidad")
guardar(fig, "02_estado_obras.png")
plt.close()

# =========================
# 3. DURACIÓN
# =========================
fig, ax = plt.subplots(figsize=(8, 5))
df["duracion_dias"].dropna().plot(kind="hist", bins=25, ax=ax)
ax.set_title("Distribución de duración de obras")
ax.set_xlabel("Días")
guardar(fig, "03_duracion_obras.png")
plt.close()

# =========================
# 4. TIPOS DE OBRA
# =========================
fig, ax = plt.subplots(figsize=(10, 5))
df["tipusobra"].value_counts().head(10).plot(kind="bar", ax=ax)
ax.set_title("Tipos de obra más frecuentes")
ax.set_xlabel("Tipo")
ax.set_ylabel("Cantidad")
plt.xticks(rotation=45)
guardar(fig, "04_tipos_obra.png")
plt.close()