# 1.- 🌍 Barcelona Open Data ETL
---
<!-- markdownlint-disable MD033 -->
<p align="center">
  <img src="documentacion/imagenes/banner.png" width="100%" alt="Imagen logo principal"/>
</p>
<!-- markdownlint-enable MD033 -->

 - Video:▶️[Python,Streamlite,Ploty](https://youtu.be/86ETKryHBPw)

Proyecto de Ingeniería de Datos que desarrolla un pipeline ETL completo para la descarga, transformación, almacenamiento y análisis de datos abiertos del Ayuntamiento de Barcelona.

La solución integra extracción automática, procesamiento con Pandas, almacenamiento en SQLite y PostgreSQL, consultas SQL y un dashboard interactivo desarrollado con Streamlit para la exploración de indicadores y visualizaciones.



---


## 2.- 🎯 Objetivos del proyecto

Este proyecto ha sido desarrollado como portfolio técnico para demostrar conocimientos en Ingeniería de Datos mediante la construcción de un pipeline ETL completo.

Los principales objetivos son:

- Consumir datos abiertos mediante APIs públicas (CKAN).
- Automatizar la extracción de datasets.
- Limpiar y transformar datos utilizando Pandas.
- Almacenar la información en una base de datos SQLite.
- Ejecutar consultas SQL para obtener indicadores.
- Generar visualizaciones de forma automática.
- Aplicar buenas prácticas de desarrollo con Git, GitHub y CI/CD.

---

## 3.- 📌 Características principales

- Pipeline ETL automatizado.
- Descarga de datos desde Open Data BCN.
- Transformación y limpieza con Pandas.
- Almacenamiento en SQLite y PostgreSQL.
- Dashboard interactivo con Streamlit.
- KPIs, mapas y visualizaciones con Plotly.
- Consultas SQL y Business Intelligence.
- Exportación de resultados en CSV.
- Pruebas automatizadas e integración continua.

---

## 4.- 🛠 Tecnologías utilizadas

| Tecnología | Uso |
| --- | --- |
| Python 3.10 | Desarrollo del pipeline ETL |
| Pandas | Limpieza y transformación de datos |
| PostgreSQL | Base de datos analítica |
| SQLite | Almacenamiento de datos |
| SQLAlchemy | Acceso a BD |
| Streamlit | Dashboard |
| Plotly | Visualizaciones |
| Requests | Descarga automática del dataset |
| Pytest | Pruebas automatizadas |
| GitHub Actions | Integración continua (CI) |

| TECNOLOGÍAS | | | | |
| --- | --- | --- | --- | --- |
| ![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python) | ![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas) | ![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite) | ![Pytest](https://img.shields.io/badge/Pytest-Passing-success?logo=pytest) | ![CI](https://github.com/israelmellado/datos-abiertos-barcelona-etl/actions/workflows/python-tests.yml/badge.svg) |
| ![GitHub last commit](https://img.shields.io/github/last-commit/israelmellado/datos-abiertos-barcelona-etl) | ![GitHub repo size](https://img.shields.io/github/repo-size/israelmellado/datos-abiertos-barcelona-etl) | ![GitHub stars](https://img.shields.io/github/stars/israelmellado/datos-abiertos-barcelona-etl?style=social) | ![License](https://img.shields.io/badge/License-MIT-green) | |


---

## 📊 Fuente de datos

**Dataset:** Obras en el espacio público de Barcelona.

**Proveedor:** Ayuntamiento de Barcelona – Open Data BCN.

**Información disponible:**

- Código de la obra.
- Distrito y barrio.
- Tipo de actuación.
- Estado de la obra.
- Fechas de inicio y finalización.
- Presupuesto de licitación.
- Presupuesto de adjudicación.
- Empresa promotora.
- Empresa constructora.
- Geometría (WGS84).



## 5.- 🏗️ Arquitectura del sistema

El proyecto implementa un pipeline ETL completo para la obtención, procesamiento y análisis de datos abiertos del Ayuntamiento de Barcelona.

```text
        Open Data BCN
              │
              ▼
          Extracción
              │
              ▼
          Transformación
              │
              ▼
          Base de datos
       (SQLite / PostgreSQL)
              │
         ┌────┴─────┐
         ▼          ▼
 Consultas SQL   Dashboard
                    │
              KPIs · BI · Mapas
```

---

## 6.- 📸 Vista previa

![Dashboard](documentacion/imagenes/dashboard.png)

## 📈 Visualizaciones

El pipeline genera automáticamente los siguientes gráficos:

### 📍 Obras por distrito

Distribución del número de obras públicas por distrito de Barcelona.

![Obras por distrito](documentacion/imagenes/01_obras_por_distrito.png)

### 🚧 Estado de las obras

Resumen del estado de ejecución de las actuaciones registradas en el dataset.

![Estado de las obras](documentacion/imagenes/02_estado_obras.png)


### 📅 Duración de las obras

Distribución de la duración de las obras expresada en días.

![Duración de las obras](documentacion/imagenes/03_duracion_obras.png)

### 🏗 Tipología de actuaciones

Clasificación de las obras según el tipo de actuación realizada.

![Tipos de obra](documentacion/imagenes/04_tipos_obra.png)

---
## 7.- ⚙️ Instalación

Clona el repositorio:

```bash
git clone https://github.com/israelmellado/datos-abiertos-barcelona-etl.git
cd datos-abiertos-barcelona-etl
```

Crea un entorno virtual:

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```
---

## 8.- ▶️ Ejecución

Para ejecutar el pipeline completo:

```bash
python codigo/pipeline.py
```
```bash
streamlit run codigo/dashboard/app.py
```
---
---
## 9.-  📂 Estructura del proyecto

```text
barcelona-open-data-etl/
├── .venv/ (Entorno virtual de Python)
├── base_datos/
│   ├── consultas_bi/
│   │   ├── 01_inversion_por_distrito.sql
│   │   ├── 02_constructoras_inversion.sql
│   │   ├── 03_ahorro_licitacion.sql
│   │   ├── 04_obras_mas_largas.sql
│   │   ├── 05_presupuesto_anual.sql
│   │   ├── 06_presupuesto_mensual.sql
│   │   ├── 07_ranking_barrios.sql
│   │   ├── 08_presupuesto_por_estado.sql
│   │   ├── 09_distribucion_presupuesto.sql
│   │   └── 10_duracion_vs_presupuesto.sql
│   ├── consultas_postgres/
│   │   ├── 01_obras_por_distrito.sql
│   │   ├── 02_obras_por_estado.sql
│   │   ├── 03_duracion_media.sql
│   │   ├── 04_top_tipos_obra.sql
│   │   ├── 05_presupuesto_medio.sql
│   │   └── 06_top_constructoras.sql
│   ├── consultas_sqlite/
│   │   ├── 01_obras_por_distrito.sql
│   │   ├── 02_obras_por_estado.sql
│   │   ├── 03_duracion_media.sql
│   │   ├── 04_top_tipos_obra.sql
│   │   ├── 05_presupuesto_medio.sql
│   │   ├── 06_top_constructoras.sql
│   │   ├── 07_top_barrios.sql
│   │   ├── 08_obras_por_anio.sql
│   │   ├── 09_obras_mas_caras.sql
│   │   └── 10_constructoras_presupuesto.sql
│   ├── modelos/
│   │   ├── modelo_obras.sql
│   │   └── modelo_postgres.sql
│   └── sqlite/
│       └── barcelona.db
├── codigo/
│   ├── __init__.py
│   ├── analisis/
│   │   └── consultas.py
│   ├── base_datos/
│   │   ├── __init__.py
│   │   ├── conexion.py
│   │   ├── postgres.py
│   │   └── sqlite.py
│   ├── carga/
│   │   ├── 06_crear_bd.py
│   │   ├── 07_cargar_obras.py
│   │   └── 08_consultas_sql.py
│   ├── configuracion/
│   │   └── config.py
│   ├── dashboard/
│   │   ├── app.py
│   │   ├── assets/
│   │   ├── consultas.py
│   │   ├── datos.py
│   │   ├── filtros.py
│   │   ├── graficos.py
│   │   ├── graficos_bi.py
│   │   ├── kpis.py
│   │   ├── kpis_bi.py
│   │   ├── mapas.py
│   │   ├── tema.py
│   │   ├── utils.py
│   │   └── visualizaciones_bi.py
│   ├── extraccion/
│   │   ├── 01_buscar_datasets.py
│   │   ├── 02_descargar_obras.py
│   │   ├── inspeccionar_dataset.py
│   │   ├── obras.py
│   │   └── obras_api.py
│   ├── pipeline.py
│   ├── transformacion/
│   │   ├── 01_explorar_obras.py
│   │   └── 02_limpiar_obras.py
│   ├── utilidades/
│   │   └── logger.py
│   └── visualizacion/
│       ├── 01_graficos_obras.py
│       └── 05_dashboard_obras.py
├── configuracion/
├── datos/
│   ├── crudos/
│   │   └── obres_espai_public.csv
│   └── procesados/
│       └── obres_limpias.csv
├── documentacion/
│   ├── analisis_fuentes_datos.md
│   ├── arquitectura_etl.md
│   ├── decisiones_tecnicas.md
│   ├── imagenes/
│   │   ├── 01_obras_por_distrito.png
│   │   ├── 02_estado_obras.png
│   │   ├── 03_duracion_obras.png
│   │   ├── 04_tipos_obra.png
│   │   ├── banner.png
│   │   └── dashboard.png
│   └── modelo_base_datos.md
├── logs/
│   └── pipeline.log
├── notebooks/
├── pruebas/
│   ├── __init__.py
│   ├── test_bd.py
│   ├── test_config.py
│   ├── test_consultas.py
│   ├── test_dashboard.py
│   ├── test_extraccion.py
│   ├── test_logger.py
│   └── test_transformacion.py
├── LICENSE
├── README.md
├── ejecutar_etl.bat
├── ejecutar_etl.py
├── pyproject.toml
└── requirements.txt

```
---

## 10.- 📊 Dashboard y Business Intelligence

El proyecto incorpora un dashboard interactivo desarrollado con **Streamlit** para explorar los datos de las obras públicas de Barcelona de forma visual.

Entre sus funcionalidades destacan:

- 📈 KPIs generales del dataset.
- 🗺️ Mapa interactivo de las obras.
- 📊 Gráficos dinámicos con Plotly.
- 📋 Estadísticas descriptivas.
- 🧾 Consultas SQL predefinidas.
- 💼 Consultas de Business Intelligence ejecutadas directamente sobre PostgreSQL.
- 📥 Exportación de resultados en formato CSV.

Las consultas BI permiten analizar indicadores como:

- Inversión por distrito.
- Ranking de constructoras.
- Ahorro entre licitación y adjudicación.
- Evolución anual y mensual del presupuesto.
- Presupuesto por estado de la obra.
- Distribución de presupuestos.
- Relación entre duración e inversión.

---

## 11.- 🧪 Calidad del software

El proyecto aplica buenas prácticas de desarrollo para garantizar la calidad y mantenibilidad del código.

Incluye:

- Pruebas automatizadas con **Pytest**.
- Integración continua mediante **GitHub Actions**.
- Formateo automático con **Black**.
- Análisis estático con **Ruff**.
- Organización modular del código.
- Sistema de logging para el pipeline ETL.

Las pruebas verifican los principales componentes del proyecto, incluyendo la extracción, transformación, carga de datos, consultas SQL, dashboard y configuración.

---

## 12.- 🚀 Estado del proyecto

Actualmente el proyecto dispone de:

- ✅ Pipeline ETL completamente funcional.
- ✅ Soporte para SQLite y PostgreSQL.
- ✅ Dashboard interactivo con Streamlit.
- ✅ KPIs, mapas y visualizaciones.
- ✅ Consultas SQL y Business Intelligence.
- ✅ Exportación de resultados.
- ✅ Pruebas automatizadas.
- ✅ Integración continua (CI).

---

### 📌 Algunas mejoras

Algunas funcionalidades previstas para futuras versiones son:

- Contenerización mediante Docker.
- Despliegue del dashboard en la nube.
- Incorporación de nuevos conjuntos de datos abiertos.
- Exportación de informes en PDF y Excel.
- Nuevos indicadores y visualizaciones analíticas.

---

## 13.- 👤 Autor

### Israel Mellado

Proyecto desarrollado como portfolio técnico para demostrar competencias en Ingeniería de Datos mediante la construcción de un pipeline ETL completo, análisis de datos y desarrollo de dashboards interactivos.

[GitHub público](https://github.com/israelmellado)

---

### 📄 Licencia

Este proyecto se distribuye con fines educativos y de portfolio.

Los datos utilizados pertenecen al portal **Open Data Barcelona** y están sujetos a las condiciones de uso establecidas por el Ayuntamiento de Barcelona.

---

### ⭐ Si te ha resultado interesante

Si este proyecto te ha servido como referencia o te ha parecido útil, puedes darle una ⭐ al repositorio.

Toda sugerencia, mejora o contribución será bienvenida.


