# 🌍 Barcelona Open Data ETL

Proyecto de ingeniería de datos que construye un pipeline ETL (Extract, Transform, Load) utilizando datos abiertos de la ciudad de Barcelona y fuentes oficiales de medio ambiente.

El objetivo es extraer datos públicos, procesarlos, almacenarlos en una base de datos y generar indicadores para análisis y visualización.

---

## 🎯 Objetivo del proyecto

Diseñar e implementar un sistema automatizado de datos que permita:

- Extraer datos de APIs públicas:
  - Obras públicas de Barcelona (Open Data BCN)
  - Calidad del aire (Ministerio para la Transición Ecológica)

- Transformar y limpiar los datos.
- Almacenarlos en una base de datos relacional.
- Generar consultas analíticas.
- Crear visualizaciones para análisis de tendencias.

---

## 🧱 Arquitectura del sistema

```text
APIs públicas
     │
     ▼
Extracción (Python - requests)
     │
     ▼
Transformación (Pandas)
     │
     ▼
Base de datos (PostgreSQL)
     │
     ▼
Consultas SQL
     │
     ▼
Dashboard (Streamlit / Power BI)
📊 Fuentes de datos
🏗️ Obras públicas - Barcelona
Portal: Open Data BCN
Información:
Obras en curso
Estado de ejecución
Ubicación geográfica
Fechas de inicio y fin
🌫️ Calidad del aire
Fuente: Ministerio para la Transición Ecológica
Variables:
NO₂
PM10
PM2.5
Ozono (O₃)
Datos horarios y diarios por estación
🛠️ Tecnologías utilizadas
Python 3.10+
Pandas
Requests
PostgreSQL
SQL
Git & GitHub
Jupyter Notebook (exploración)
Streamlit (visualización futura)
📁 Estructura del proyecto
datos-abiertos-barcelona-etl/
│
├── configuracion/
├── datos/
│   ├── crudos/
│   ├── procesados/
│   └── archivo/
│
├── codigo/
│   ├── extraccion/
│   ├── transformacion/
│   ├── carga/
│   └── utilidades/
│
├── base_datos/
├── documentacion/
├── notebooks/
└── pruebas/

🚀 Estado del proyecto

✔ Estructura inicial creada
✔ Repositorio Git inicializado
✔ Primer commit realizado
⏳ Extracción de datos (pendiente)
⏳ Pipeline ETL (en desarrollo)
⏳ Dashboard (pendiente)

🧠 Qué demuestra este proyecto

Este proyecto demuestra habilidades en:

Consumo de APIs REST
Procesamiento de datos con Python
Limpieza y transformación de datos
Modelado de bases de datos
SQL para análisis
Construcción de pipelines ETL
Buenas prácticas de Git y estructura de proyectos
📌 Próximas mejoras
Automatización del pipeline (cron / Airflow)
Contenedorización con Docker
Tests automatizados
Dashboard interactivo
Despliegue en la nube
Integración con más fuentes de datos
👤 Autor

Proyecto desarrollado como parte de un portfolio de ingeniería de datos.