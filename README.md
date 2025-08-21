
# Retail Sales Trend Seasonal and Marketing Data QA

![Badge en Desarollo](https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green)

This project applies automated Data QA checks to a retail sales with seasonal trends and marketing data.
It ensure data quality by detecting missing values, duplicates, out-of-range values and inconsistencies, improving confidence in analysisi.

## Motivation

## Dataset
The dataset "Retail Sales Data with Seasonal Trends & Marketing" contains sales, units sold, discount percentages, marketing spend, and seasonal indicators for multiple stores. 
Source: [Kaggle Dataset](https://www.kaggle.com/datasets/delafuenteo/retail-sales-csv/data)

## instalation

**install kagglehub**

pip install kagglehub


## Expected Results






--------------
## Important 

 En proyectos de **Data QA / Data Quality** no siempre hay un único estándar universal, pero sí existen **marcos y herramientas reconocidos** que sirven como guía para definir los **criterios de calidad de datos (QA Checks)**:

### 🔹 Estándares / Marcos de referencia

1. **ISO 8000 (Data Quality)**
   Norma internacional sobre gestión de calidad de datos. Define principios como:

   * **Completitud** (no faltan datos relevantes)
   * **Exactitud** (los valores corresponden a la realidad)
   * **Consistencia** (sin contradicciones entre campos)
   * **Validez** (datos en rangos/formato correcto)
   * **Unicidad** (sin duplicados innecesarios)
   * **Actualidad** (fechas y tiempos coherentes).

2. **DAMA-DMBOK (Data Management Body of Knowledge)**
   Marco de referencia de DAMA International. Recomienda dimensiones clásicas de calidad de datos:

   * **Validez**
   * **Precisión**
   * **Completitud**
   * **Consistencia**
   * **Integridad**

3. **TDQM (Total Data Quality Management)** – MIT
   Metodología que enfatiza procesos iterativos de medición y mejora continua de la calidad de datos.

Herramientas usadas en la práctica

En Python/pandas podemos implementarlo manualmente con **pytest** y funciones, pero en la industria también se usan frameworks especializados:

* **Great Expectations** → librería Python para definir expectativas de calidad en datasets (ej: “no más del 5% de nulos en esta columna”).
* **Pandera** → extensión de pandas para validar esquemas y aplicar checks en DataFrames.
* **Deequ** (Amazon, en Scala/Python wrapper) → validación de calidad de datos en pipelines grandes.

