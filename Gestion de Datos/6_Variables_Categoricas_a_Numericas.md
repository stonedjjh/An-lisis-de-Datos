# 6. Transformación de Variables Categóricas a Cuantitativas

En el análisis de datos y machine learning, la gran mayoría de los modelos estadísticos y algoritmos predictivos **solo aceptan números como entrada**, y no pueden procesar directamente palabras, textos o cadenas de caracteres (strings/objects).

Por lo tanto, cuando tenemos una variable categórica (texto), estamos obligados a transformarla en algún formato numérico antes de poder entrenar nuestro modelo.

## El Problema: Variables Categóricas
Imaginemos que tenemos una característica (columna) llamada "tipo de combustible" (`fuel`) en un dataset de automóviles. Esta columna tiene dos valores posibles en formato de texto:
- `gas`
- `diesel`

Si intentamos alimentar un modelo matemático con la palabra "gas", nos arrojará un error.

## La Solución: Variables Ficticias (*Dummy Variables*)
La técnica estándar para solucionar este problema a menudo se llama **One-Hot Encoding** (codificación One-Hot). Consiste en convertir cada categoría única en una nueva característica (columna independiente), y asignarle un valor numérico binario (`0` o `1`).

### ¿Cómo funciona?
1. Se añaden nuevas columnas, una por cada valor único presente en la variable original. En nuestro ejemplo, en lugar de una columna `fuel`, crearemos dos nuevas columnas: `gas` y `diesel`.
2. Si el valor original de un auto (Auto A) era `gas`, le asignamos un `1` a la nueva columna `gas` y un `0` a la columna `diesel`.
3. Si el valor original de un auto (Auto B) era `diesel`, le asignamos un `0` a la nueva columna `gas` y un `1` a la columna `diesel`.

De esta manera matemática, la información categórica original se preserva íntegramente usando puros números.

---

## Implementación en Python (con Pandas)

Transformar variables categóricas a numéricas en Python es extremadamente sencillo gracias al método integrado de Pandas llamado `get_dummies()`.

```python
import pandas as pd

# El método get_dummies convierte automáticamente las variables de texto en variables "dummy" (0 o 1)
dummy_variable_1 = pd.get_dummies(df['fuel'])
```

Al ejecutar este simple método, Pandas automáticamente generará una lista de números y creará el dataframe correspondiente donde cada categoría de la variable original se ha convertido en una columna binaria independiente.
