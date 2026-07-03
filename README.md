# 🌍Barcelona Open Data ETL

Proyecto de Ingeniería de Datos que implementa un pipeline ETL (Extract, Transform, Load) utilizando datos abiertos del Ayuntamiento de Barcelona.

El objetivo es demostrar competencias en extracción de datos desde APIs públicas, procesamiento con Python, análisis exploratorio y generación de visualizaciones siguiendo buenas prácticas de desarrollo.

---

## 🎯Objetivos del proyecto

+ Consumir datos abiertos mediante APIs REST (CKAN).
+ Automatizar la extracción de datasets públicos.
+ Limpiar y transformar los datos utilizando Pandas.
+ Generar un conjunto de datos preparado para análisis.
+ Obtener indicadores y métricas relevantes.
+ Crear visualizaciones automáticas.
+ Preparar los datos para su futura carga en una base de datos relacional.

---

## 🧱Arquitectura del sistema

```text
Open Data BCN 
  │
  ▼ 
Extracción (Python + Requests) 
  │ 
  ▼
Datos crudos (CSV) 
  │ 
  ▼
Transformación (Pandas) 
  │
  ▼
CSV procesado
  │ 
  ▼ 
Análisis (KPIs) 
  │
  ▼
Visualizaciones (Matplotlib)
  │
  ▼ 
SQLite
  │
  ├── Consultas SQL
  │
  └── Dashboard (Matplotlib)
```

## 📊 Fuente de datos actual

## 🏗 Obras públicas de Barcelona

Fuente: Open Data BCN

Información disponible:

+ Obras en curso
+ Estado de ejecución
+ Distrito y barrio
+ Fechas de inicio y finalización
+ Presupuestos
+ Empresa constructora
+ Geometría de las actuaciones

## 🛠 Tecnologías utilizadas

+ Python 3.10
+ Pandas
+ Requests
+ Matplotlib
+ Git
+ GitHub
+ Jupyter Notebook (exploración)
+ SQLite
+ PostgreSQL (mejora futura)

---

```📁Estructura del proyecto
barcelona-open-data-etl/ 
│ 
├── codigo/
│   ├──pruebas/
│   ├── analisis/ 
│   ├── extraccion/ 
│   ├── transformacion/ 
│   ├── visualizacion/ 
│   ├── configuracion/
│   ├── carga/ 
│   └── utilidades/ 
│   
│ 
├── datos/ 
│    ├── crudos/ 
│    ├── procesados/ 
│    └── archivo/ 
│    
├── documentacion/ 
│   ├── imagenes/
│   ├── arquitectura_etl.md
│   ├── decisiones_tecnicas.md
│   └── analisis_fuentes_datos.md 
│    
├── notebooks/ 
├── pruebas/ 
│
├── base_datos/ 
│   ├── modelos/
│   ├── consultas/
│   └── sqlite/ 
│
├── .venv/
├── README.md 
├── requirements.txt 
└── .gitignore
```

## 🚀Estado del proyecto

+ ✅ Estructura profesional del proyecto
+ ✅ Repositorio Git y GitHub
+ ✅ Pipeline ETL automatizado
+ ✅ Descarga automática del dataset
+ ✅ Limpieza y transformación
+ ✅ Base de datos SQLite
+ ✅ Consultas SQL
+ ✅ Generación automática de gráficos
+ ✅ Sistema de logging
+ ⏳ Dashboard interactivo (Streamlit)
+ ⏳ Integración de nuevas fuentes
+ ⏳ PostgreSQL

## 🧠Qué demuestra este proyecto

Este proyecto demuestra habilidades en:

+ 1 Consumo de APIs REST
+ 2 Procesamiento de datos con Python
+ 3 Limpieza y transformación de datos
+ 4 Modelado de bases de datos
+ 5 SQL para análisis
+ 6 Construcción de pipelines ETL
+ 7 Buenas prácticas de Git y estructura de proyectos

## 📌Próximas mejoras

+ ⬜ Incorporar nuevos datasets de Open Data BCN.
+ ⬜ Migrar la base de datos a PostgreSQL.
+ ⬜ Crear un dashboard interactivo con Streamlit.
+ ⬜ Añadir pruebas unitarias con pytest.
+ ⬜ Automatizar el despliegue con GitHub Actions.
+ ⬜ Contenerizar el proyecto con Docker.
+ ⬜ Parametrizar el pipeline mediante argparse.

## 📊Resultados obtenidos

El pipeline procesa automáticamente el conjunto de datos, elimina registros duplicados, calcula la duración de las obras, carga la información en SQLite, ejecuta consultas SQL predefinidas y genera visualizaciones listas para su análisis.

+ Número de obras por distrito.
+ Estado de ejecución.
+ Distribución temporal de las obras.
+ Tipología de actuaciones.
+ Análisis de presupuestos.

### Obras por distrito

![Obras por distrito](documentacion/imagenes/01_obras_por_distrito.png)

### Estado de las obras

![Estado de las obras](documentacion/imagenes/02_estado_obras.png)

### Duración de las obras

![Duración](documentacion/imagenes/03_duracion_obras.png)

### Tipos de obra

![Tipos de obra](documentacion/imagenes/04_tipos_obra.png)

## 🚀 Competencias demostradas

Este proyecto demuestra conocimientos prácticos en:

+ Consumo de APIs REST (CKAN).
+ Automatización de extracción de datos.
+ Procesamiento de datos con Pandas.
+ Limpieza y transformación de datos.
+ Análisis exploratorio (EDA).
+ Generación de visualizaciones con Matplotlib.
+ Organización de proyectos ETL.
+ Control de versiones mediante Git y GitHub.
+ SQL sobre SQLite.
+ Registro de eventos mediante logging.

## 👤Autor

Proyecto desarrollado por Israel Mellado como portfolio técnico para demostrar competencias en Ingeniería y Análisis de Datos mediante el desarrollo de un pipeline ETL con datos abiertos.
