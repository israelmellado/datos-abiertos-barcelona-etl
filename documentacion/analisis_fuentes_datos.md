# 1. 🏗️ Open Data BCN (Obras públicas)
## 📌 Descripción

El portal de datos abiertos del Ayuntamiento de Barcelona proporciona información sobre múltiples áreas de la ciudad. Para este proyecto utilizaremos el dataset de obras públicas en curso.

## 🔍 Tipo de acceso

- Plataforma: Open Data BCN
- Acceso: descarga directa y/o API (según dataset)
- Formato habitual:
- JSON
- CSV
- XML (menos frecuente)

## 📊 Información disponible

Los datos de obras suelen incluir:

- Nombre de la obra
- Estado (en curso / finalizada / planificada)
- Distrito y barrio
- Fecha de inicio
- Fecha prevista de finalización
- Tipo de intervención
- Ubicación geográfica (latitud / longitud en algunos casos)

## 🧠 Uso en el proyecto

Estos datos permitirán:

- Analizar obras activas por distrito
- Estudiar duración de proyectos
- Visualizar obras en un mapa
- Detectar zonas con mayor actividad urbanística

## ⚠️ Consideraciones
- Puede haber datos incompletos (fechas o ubicación)
- Algunos datasets se actualizan de forma periódica, no en tiempo real
- La estructura puede variar entre conjuntos de datos

# 2. 🌫️ Ministerio para la Transición Ecológica (Calidad del aire)
## 📌 Descripción

El Ministerio publica datos sobre la calidad del aire en España mediante estaciones de medición distribuidas por todo el territorio.

## 🔍 Tipo de acceso

- 1 API pública y datasets descargables
- 2 Formatos:
- 3 JSON (API)
- 4 CSV (descargas históricas)

## 📊 Información disponible

Las estaciones de medición registran:

- NO₂ (dióxido de nitrógeno)
- PM10
- PM2.5
- Ozono (O₃)
- SO₂
- Datos horarios o diarios
- Identificador de estación
- Ubicación geográfica

## 🧠 Uso en el proyecto

Permite:

- Analizar evolución de contaminación en Barcelona
- Comparar zonas de la ciudad
- Detectar picos de contaminación
- Relacionar contaminación con obras públicas

## ⚠️ Consideraciones

- Alta granularidad (muchos datos por día)
- Necesidad de limpieza y agregación
- Algunas estaciones pueden tener datos faltantes

# 3. 🔎 Conclusión técnica

Este proyecto combina dos fuentes complementarias:

## 🏗️ Datos urbanos (obras públicas)
## 🌫️ Datos ambientales (calidad del aire)

Esto permite construir un sistema de análisis que puede responder preguntas como:

- ¿Aumenta la contaminación en zonas con más obras?
- ¿Qué distritos tienen mayor actividad urbana?
- ¿Cómo evoluciona la calidad del aire en el tiempo?

## 🧱 Implicación para el ETL

El sistema deberá:

- 1 Extraer datos de dos fuentes diferentes
- 2 Normalizar estructuras distintas
- 3 Almacenar en una base de datos relacional
- 4 Permitir análisis cruzado entre datasets