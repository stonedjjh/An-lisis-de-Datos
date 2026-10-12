# Módulo 1: Importación de conjuntos de datos

Este módulo aborda los fundamentos de la adquisición, lectura, primera inspección y extracción de datos en Python, preparando la base sobre la cual se realizarán las fases de limpieza, exploración y modelado.

---

## Objetivos de Aprendizaje

- Comprender la naturaleza y estructura de un dataset (atributos, registros, variables objetivo y formatos como CSV).
- Conocer el ecosistema de paquetes esenciales de Python (computación científica, visualización y machine learning).
- Importar y exportar datasets utilizando Pandas (`read_csv`, `to_csv`), controlando rutas y parámetros clave como cabeceras (`headers`).
- Realizar la primera inspección diagnóstica de los datos mediante tipos de datos (`dtypes`), resúmenes estadísticos (`describe`) e información general (`info`).
- Conocer los conceptos clave del estándar Python DB-API (`Connection`, `Cursor`, `commit`, `rollback`, `close`) para consultar bases de datos relacionales desde scripts de Python.

---

## Índice de Temas y Documentos

| # | Tema / Archivo | Resumen de Contenido |
|---|---|---|
| 1 | [1. Comprender los datos](./1_Comprender_los_datos.md) | Introducción al dataset de ejemplo (precios de autos usados), características del formato CSV, manejo de archivos sin cabeceras (*headers*), definición de *features* y variable objetivo (*target* / *label*). |
| 2 | [2. Paquetes Python para Ciencia de Datos](./2_Paquetes_Python_para_Ciencia_de_Datos.md) | Panorama de librerías esenciales agrupadas por propósito: computación científica (Pandas, NumPy, SciPy), visualización (Matplotlib, Seaborn) y modelos algorítmicos (Scikit-Learn, Statsmodels). |
| 3 | [3. Importar y Exportar Datos en Python](./3_Importar_y_Exportar_Datos_en_Python.md) | Lectura con `pd.read_csv()`, configuración de parámetros (`header=None`, nombres de columnas), exploración preliminar con `head()` / `tail()`, y exportación con `to_csv()`. |
| 4 | [4. Introducción al Análisis de Datos](./4_Introduccion_al_Analisis_de_Datos.md) | Métodos de diagnóstico inicial en Pandas: verificación de tipos con `df.dtypes`, análisis estadístico univariado con `df.describe()` (incluyendo variables categóricas con `include='all'`), y diagnóstico de memoria y valores no nulos con `df.info()`. |
| 5 | [5. Acceso a Bases de Datos desde Python](./5_Acceso_a_Bases_de_Datos.md) | Uso de Python DB-API para conectar con RDBMS (MySQL, PostgreSQL, SQLite); objetos de conexión (`Connection`), objetos de ejecución (`Cursor`), consultas SQL y ciclo de vida de conexión (`close`). |

---

## Herramientas y Métodos Clave

```python
# Importación e inspección básica en Pandas
import pandas as pd

# Lectura sin cabecera y asignación de nombres
df = pd.read_csv("ruta/al/dataset.csv", header=None)
df.columns = ["col1", "col2", "precio"]

# Diagnóstico rápido
df.head()
df.dtypes
df.describe(include="all")
df.info()

# Exportación
df.to_csv("datos_procesados.csv", index=False)
```

---

## Ejercicios Prácticos Relacionados

Los ejercicios prácticos correspondientes a los conceptos de este módulo se encuentran en la carpeta [`Ejercicios_Practicos/Importacion de Conjuntos de Datos`](../Ejercicios_Practicos/Importacion%20de%20Conjuntos%20de%20Datos):

- [Precios de coches usados (automobile)](../Ejercicios_Practicos/Importacion%20de%20Conjuntos%20de%20Datos/automobile): Práctica completa de importación de dataset CSV sin cabeceras, asignación de nombres de columnas, inspección de tipos de datos (`dtypes`), resumen estadístico (`describe`) y exportación. Incluye notebook [`.ipynb`](../Ejercicios_Practicos/Importacion%20de%20Conjuntos%20de%20Datos/automobile/Precios%20de%20coches%20usados.ipynb), script [`.py`](../Ejercicios_Practicos/Importacion%20de%20Conjuntos%20de%20Datos/automobile/Precios%20de%20coches%20usados.py) y dataset [`automobile.csv`](../Ejercicios_Practicos/Importacion%20de%20Conjuntos%20de%20Datos/automobile/automobile.csv).
- [Precios para portátiles (portatil)](../Ejercicios_Practicos/Importacion%20de%20Conjuntos%20de%20Datos/portatil): Práctica de carga de datos desde URL/archivo local, exploración inicial de atributos de laptops y análisis descriptivo preliminar. Incluye notebook [`.ipynb`](../Ejercicios_Practicos/Importacion%20de%20Conjuntos%20de%20Datos/portatil/Precios%20para%20portátiles.ipynb), script [`.py`](../Ejercicios_Practicos/Importacion%20de%20Conjuntos%20de%20Datos/portatil/Precios%20para%20portátiles.py) y dataset [`laptops.csv`](../Ejercicios_Practicos/Importacion%20de%20Conjuntos%20de%20Datos/portatil/laptops.csv).
