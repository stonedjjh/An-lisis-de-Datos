# Módulo 3: Análisis Exploratorio de Datos (EDA)

El Análisis Exploratorio de Datos (Exploratory Data Analysis - EDA) es el proceso crítico que precede al modelado matemático y predictivo. Su objetivo principal es sintetizar las características clave del conjunto de datos, identificar patrones, detectar anomalías o valores atípicos (*outliers*), y determinar qué variables tienen el mayor impacto predictivo sobre la variable objetivo (*target*).

---

## Objetivos de Aprendizaje

- Aplicar estadísticas descriptivas numéricas (`describe`) y conteos de frecuencia categórica (`value_counts`) para evaluar la distribución de los datos.
- Visualizar distribuciones univariadas y multivariadas con diagramas de caja (*Box Plots*) y gráficos de dispersión (*Scatter Plots*).
- Agrupar datos por categorías múltiples mediante `groupby()` y operaciones de agregación estadística (`mean()`).
- Estructurar y rotar vistas tabulares complejas mediante Tablas Dinámicas (`pivot()`).
- Interpretar densidades y relaciones multidimensionales mediante Mapas de Calor (*Heatmaps*) y pseudocolor (`plt.pcolor`).
- Seleccionar y dominar la biblioteca gráfica adecuada en Python (Matplotlib vs. Seaborn) según el nivel de personalización y abstracción estadística requerida.

---

## Índice de Temas y Documentos

| # | Tema / Archivo | Resumen de Contenido |
|---|---|---|
| 1 | [1. Análisis Exploratorio de Datos](./1_Analisis_Exploratorio_de_Datos.md) | Introducción al EDA, objetivos de diagnóstico, identificación de características predictivas clave sobre el precio del vehículo y resumen de técnicas principales (descriptivas, GroupBy, ANOVA y correlación). |
| 2 | [2. Estadísticas Descriptivas y Visualización](./2_Estadisticas_Descriptivas.md) | Resúmenes de variables numéricas (`describe`), frecuencias categóricas (`value_counts`), anatomía e interpretación de Box Plots con outliers, y gráficos de dispersión para relaciones lineales. |
| 3 | [3. GroupBy y Tablas Dinámicas](./3_GroupBy_en_Python.md) | Agrupación multivariable con `groupby()`, transformación matricial con `pivot()` para tablas dinámicas y representación visual con Mapas de Calor (`pcolor` / Heatmaps). |
| 4 | [4. Creación de Gráficos en Python](./4_Creacion_de_Graficos_en_Python.md) | Catálogo práctico de visualización con Matplotlib (`plot`, `scatter`, `hist`, `bar`, `pcolor`) y Seaborn (`regplot`, `boxplot`, `residplot`, `kdeplot`, `distplot`). |

---

## Métodos y Sintaxis Clave

```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Estadísticas descriptivas
df.describe()
df["drive-wheels"].value_counts()

# 2. Agrupación y tabla dinámica
df_grp = df[["drive-wheels", "body-style", "price"]].groupby(
    ["drive-wheels", "body-style"], as_index=False
).mean()
df_pivot = df_grp.pivot(index="drive-wheels", columns="body-style", values="price")

# 3. Mapa de calor de tabla dinámica
plt.pcolor(df_pivot, cmap="RdBu")
plt.colorbar()
plt.show()

# 4. Gráficos estadísticos con Seaborn
sns.boxplot(x="drive-wheels", y="price", data=df)
sns.regplot(x="engine-size", y="price", data=df)
sns.residplot(data=df, x="engine-size", y="price")
```

---

## Ejercicios Prácticos Relacionados

Los scripts y conjuntos de datos para ejercitar los conceptos de este módulo se encuentran en la carpeta [`Ejercicios_Practicos/Análisis exploratorio de datos`](../Ejercicios_Practicos/Análisis%20exploratorio%20de%20datos):

- [Precios de coches usados](../Ejercicios_Practicos/Análisis%20exploratorio%20de%20datos/Precios%20de%20coches%20usados): Análisis exploratorio completo con cálculo de correlación de Pearson, mapas de calor, análisis de varianza (ANOVA), pruebas estadísticas sobre características de vehículos y scripts ejecutables ([`analisis_exploratorio_datos_coches.py`](../Ejercicios_Practicos/Análisis%20exploratorio%20de%20datos/Precios%20de%20coches%20usados/analisis_exploratorio_datos_coches.py), [`Exploratory_data_analysis_cars.py`](../Ejercicios_Practicos/Análisis%20exploratorio%20de%20datos/Precios%20de%20coches%20usados/Exploratory_data_analysis_cars.py)) junto a su dataset [`automobileEDA.csv`](../Ejercicios_Practicos/Análisis%20exploratorio%20de%20datos/Precios%20de%20coches%20usados/automobileEDA.csv).
- [Precios de los portátiles](../Ejercicios_Practicos/Análisis%20exploratorio%20de%20datos/Precios%20de%20los%20portátiles): Práctica de exploración univariada y bivariada en datos de laptops ([`analisis_exploratorio_datos_portatiles.py`](../Ejercicios_Practicos/Análisis%20exploratorio%20de%20datos/Precios%20de%20los%20portátiles/analisis_exploratorio_datos_portatiles.py), [`practice_Exploratory_data_analysis.py`](../Ejercicios_Practicos/Análisis%20exploratorio%20de%20datos/Precios%20de%20los%20portátiles/practice_Exploratory_data_analysis.py)) usando el dataset [`laptop_pricing_dataset_mod2.csv`](../Ejercicios_Practicos/Análisis%20exploratorio%20de%20datos/Precios%20de%20los%20portátiles/laptop_pricing_dataset_mod2.csv).
