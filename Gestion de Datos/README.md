# Módulo 2: Gestión de Datos (Data Wrangling)

Este módulo se enfoca en las técnicas fundamentales de preprocesamiento, limpieza y transformación de datos (Data Wrangling / Data Cleaning). Su objetivo es convertir datos crudos e imperfectos en un formato estructurado, homogéneo y matemáticamente apto para el análisis exploratorio y el entrenamiento de modelos de Machine Learning.

---

## Objetivos de Aprendizaje

- Dominar la manipulación de datos a nivel de Series y columnas en Pandas.
- Identificar y tratar valores perdidos (*missing values* / `NaN`) mediante eliminación selectiva (`dropna`) o imputación estadística (`replace` con media o moda).
- Formatear y estandarizar datos: unificación de expresiones textuales, conversión matemática de unidades y corrección de tipos de datos (`dtypes`, `astype`).
- Aplicar técnicas de normalización de variables numéricas continuas: Simple Feature Scaling, Min-Max y Z-score.
- Implementar agrupamiento numérico (*Binning*) mediante `np.linspace` y `pd.cut` para segmentar variables y reducir ruido.
- Transformar variables categóricas de texto a variables cuantitativas binarias (*Dummy Variables* / One-Hot Encoding) usando `pd.get_dummies()`.

---

## Índice de Temas y Documentos

| # | Tema / Archivo | Resumen de Contenido |
|---|---|---|
| 1 | [1. Estandarización, Normalización y Agrupación](./1_Estandarizacion_Normalizacion_Agrupacion.md) | Visión panorámica del preprocesamiento en Pandas, acceso a columnas como Series y operaciones vectorizadas directas. |
| 2 | [2. Tratamiento de Valores Perdidos](./2_Tratamiento_Valores_Perdidos.md) | Detección de datos faltantes (`NaN`), estrategias de descarte (`dropna` por filas o columnas) e imputación por promedio o moda con `replace()`. |
| 3 | [3. Formateo de Datos](./3_Formateo_de_Datos.md) | Homogeneización de texto, conversión de unidades de medida (ej. mpg a L/100km con `rename`), inspección de tipos (`dtypes`) y conversión con `astype()`. |
| 4 | [4. Normalización de Datos](./4_Normalizacion_de_Datos.md) | Justificación matemática del escalado y tres métodos prácticos: Escalado Simple (división por el máximo), Min-Max (rango 0 a 1) y Z-score (centrado en 0 con desviación estándar). |
| 5 | [5. Binning (Agrupación de Datos)](./5_Binning_Agrupacion.md) | Discretización de variables continuas en contenedores categóricos mediante `np.linspace()` y `pd.cut()`, facilitando análisis de distribución e histogramas. |
| 6 | [6. Variables Categóricas a Numéricas](./6_Variables_Categoricas_a_Numericas.md) | Creación de variables ficticias (*Dummy Variables* / One-Hot Encoding) con `pd.get_dummies()` para permitir la entrada de datos textuales a modelos matemáticos. |

---

## Métodos y Sintaxis Clave

```python
import numpy as np
import pandas as pd

# 1. Tratamiento de valores perdidos
df.dropna(subset=["price"], axis=0, inplace=True)
promedio = df["normalized-losses"].astype("float").mean()
df["normalized-losses"].replace(np.nan, promedio, inplace=True)

# 2. Formateo y tipos
df["price"] = df["price"].astype("float")
df["city-L/100km"] = 235 / df["city-mpg"]

# 3. Normalización (Min-Max y Z-Score)
df["length_minmax"] = (df["length"] - df["length"].min()) / (df["length"].max() - df["length"].min())
df["length_zscore"] = (df["length"] - df["length"].mean()) / df["length"].std()

# 4. Binning
bins = np.linspace(df["price"].min(), df["price"].max(), 4)
etiquetas = ["Bajo", "Medio", "Alto"]
df["price-binned"] = pd.cut(df["price"], bins, labels=etiquetas, include_lowest=True)

# 5. One-Hot Encoding
dummies_combustible = pd.get_dummies(df["fuel-type"])
df = pd.concat([df, dummies_combustible], axis=1)
```

---

## Ejercicios Prácticos Relacionados

Los ejercicios y notebooks correspondientes a este módulo se encuentran en la carpeta [`Ejercicios_Practicos/Manejo de datos`](../Ejercicios_Practicos/Manejo%20de%20datos):

- [Data Wrangling](../Ejercicios_Practicos/Manejo%20de%20datos): Práctica guiada integral que cubre el ciclo completo de preparación del dataset de automóviles: identificación de símbolos de interrogación (`?`), conversión e imputación de valores faltantes, formateo de unidades, normalización de dimensiones, agrupación de precios (*binning*) y generación de variables ficticias (*dummies*). Incluye notebook [`.ipynb`](../Ejercicios_Practicos/Manejo%20de%20datos/Data%20Wrangling.ipynb) y script reproducible [`.py`](../Ejercicios_Practicos/Manejo%20de%20datos/Data%20Wrangling.py).
