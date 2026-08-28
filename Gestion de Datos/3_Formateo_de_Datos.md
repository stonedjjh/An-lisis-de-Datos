# Formateo de Datos

El **formateo de datos** consiste en llevar los datos a un estándar de expresión común, permitiendo realizar comparaciones claras y significativas. Debido a que los datos suelen provenir de distintas fuentes y personas, a menudo llegan en formatos, unidades o convenciones variadas. 

Como parte fundamental de la limpieza, el formateo asegura la coherencia e interpretabilidad de la información.

## 1. Estandarización de Expresiones
Es muy normal encontrar distintas maneras de referirse a una misma cosa (por ejemplo, "N.Y.", "Ny", "NY" y "New York"). Si bien esta inconsistencia a veces es útil para detectar fraudes o anomalías, casi siempre lo que buscamos es **unificar todas las variaciones** en un solo formato estándar para facilitar el análisis estadístico posterior.

## 2. Conversión de Unidades
A veces necesitas adaptar valores numéricos a tus propias convenciones o sistemas (por ejemplo, de sistema imperial a métrico). En Python, esto se hace aplicando fórmulas directamente a toda la columna. Posteriormente, debes renombrar la columna para indicar la nueva unidad de medida.

```python
# Ejemplo: Convertir "millas por galón (mpg)" a "litros por 100 km" (fórmula: 235 / mpg)
df['city-mpg'] = 235 / df['city-mpg']

# Renombrar la columna usando el método rename para reflejar la nueva unidad
df.rename(columns={'city-mpg': 'city-L/100km'}, inplace=True)
```

## 3. Exploración y Conversión de Tipos de Datos (Data Types)
Al importar datos, Pandas puede equivocarse y asignar tipos incorrectos. Por ejemplo, podría asignar el tipo texto (`object`) a una columna de precios (que debería ser un número `int` o `float`). 

Es obligatorio identificar estos errores y convertir las columnas al tipo de dato correcto antes de empezar a crear modelos predictivos, ya que de lo contrario, el sistema tratará esos datos de manera anómala o fallará.

**Tipos de datos comunes en Pandas:**
- **Objects:** Cadenas de texto (strings, letras, palabras).
- **Int64:** Números enteros.
- **Floats:** Números reales (con puntos decimales).

### Métodos de Pandas para Tipos de Datos
- `.dtypes`: Te permite ver el tipo de dato asignado a cada columna.
- `.astype()`: Te permite convertir una columna de un tipo a otro.

```python
# Comprobar el tipo de dato de todas las columnas
print(df.dtypes)

# Convertir la columna 'price' de tipo 'object' a entero ('int')
df['price'] = df['price'].astype("int")
```
