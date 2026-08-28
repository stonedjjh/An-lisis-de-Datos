# 1. Estandarización, Normalización y Agrupación de Datos

Este documento resume las técnicas fundamentales de gestión y preprocesamiento de datos utilizando Pandas en Python, orientadas a preparar los datos para su posterior análisis y modelado estadístico.

## Técnicas Principales

1. **Estandarización de Datos**: 
   Consiste en transformar los valores de un conjunto de datos para que todos sigan el mismo formato, unidad de medida o convención.

2. **Normalización de Datos**: 
   Las distintas columnas numéricas pueden tener rangos muy diferentes, lo que hace que una comparación directa pierda el sentido. La normalización (mediante técnicas de centrado y escalado) ajusta todos los datos numéricos a un rango similar para que puedan ser comparados y evaluados correctamente.

3. **Agrupación de Datos (Binning)**: 
   Técnica que permite agrupar valores numéricos en categorías (o intervalos) más amplias. Es particularmente útil cuando se quiere comparar el comportamiento de diferentes grupos dentro de la muestra.

4. **Variables Categóricas**: 
   Para facilitar el entrenamiento de los modelos estadísticos, se requiere convertir valores categóricos (como texto o etiquetas) en representaciones numéricas.

## Manipulación de Datos en Pandas

Por lo general, en Python las operaciones se aplican a nivel de **columnas**:
- Cada **fila** representa una muestra individual (por ejemplo, un coche usado en la base de datos).
- Cada **columna** extraída del DataFrame es una **Serie de Pandas** (Pandas Series).

Puedes acceder directamente a una columna indicando su nombre. Además, Pandas permite aplicar operaciones matemáticas directas a todos los registros de una columna de forma simultánea. Por ejemplo, si deseas sumarle 1 a cada valor de una columna llamada "symboling":

``python
df['symboling'] = df['symboling'] + 1
``
