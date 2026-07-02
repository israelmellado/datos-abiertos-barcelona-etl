from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# RUTAS
# =========================
RAIZ = Path(__file__).resolve().parents[2]
ARCHIVO = RAIZ / "datos" / "procesados" / "obres_limpias.csv"

df = pd.read_csv(ARCHIVO)

# =========================
# 1. OBRAS POR DISTRITO
# =========================
plt.figure()
df["nom_districte"].value_counts().head(10).plot(kind="bar")
plt.title("Obras por distrito")
plt.xlabel("Distrito")
plt.ylabel("Número de obras")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =========================
# 2. ESTADO DE LAS OBRAS
# =========================
plt.figure()
df["estat"].value_counts().plot(kind="bar")
plt.title("Estado de las obras")
plt.xlabel("Estado")
plt.ylabel("Cantidad")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =========================
# 3. DURACIÓN MEDIA
# =========================
plt.figure()
df["duracion_dias"].dropna().plot(kind="hist", bins=20)
plt.title("Distribución de duración de obras")
plt.xlabel("Días")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.show()

# =========================
# 4. TIPOS DE OBRA
# =========================
plt.figure()
df["tipusobra"].value_counts().head(10).plot(kind="bar")
plt.title("Tipos de obra más comunes")
plt.xlabel("Tipo")
plt.ylabel("Cantidad")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =========================
# 5. PRESUPUESTO (LICITACIÓN)
# =========================
plt.figure()
df["pressupost_licitacio"].dropna().plot(kind="hist", bins=30)
plt.title("Distribución del presupuesto de licitación")
plt.xlabel("Euros")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.show()