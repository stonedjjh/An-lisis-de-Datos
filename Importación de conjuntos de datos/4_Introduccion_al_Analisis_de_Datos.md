# 4. Introducción al Análisis de Datos

Una vez que los datos han sido importados exitosamente, el siguiente paso es explorarlos. Pandas ofrece métodos integrados muy útiles para obtener una vista general, revisar los tipos de datos y analizar distribuciones estadísticas básicas, lo cual ayuda a detectar problemas rápidamente.

## 1. Revisar los Tipos de Datos (`df.dtypes`)
Es común que Pandas asigne tipos de datos automáticamente al leer un archivo basándose en la codificación. A veces, esta asignación es incorrecta.

Los tipos principales en Pandas son:
-   `object`: Funciona de manera similar a un `string` (texto) en Python.
-   `int` y `float`: Tipos numéricos estándar.
-   `datetime`: Específico para series de tiempo y fechas.

**¿Por qué es vital revisarlos?**
1.  **Detección de errores obvios:** Si una columna que debería ser el "precio" numérico de un auto aparece como tipo `object` (texto), las operaciones matemáticas fallarán. 
2.  **Aplicabilidad de funciones:** Muchas funciones matemáticas solo funcionan en columnas numéricas (`int` o `float`). Si están mal asignadas, obtendrás errores técnicos al intentar calcular promedios o desviaciones.

```python
# Muestra el tipo de dato asignado a cada columna del dataframe
df.dtypes
```

## 2. Resumen Estadístico (`df.describe()`)
El método `.describe()` devuelve un resumen de métricas estadísticas que te permite conocer la distribución matemática de los datos en cada columna (valores extremos, promedios, desviaciones).

```python
# Muestra un resumen de las columnas numéricas
df.describe()
```
Para columnas numéricas, te devolverá:
-   `count`: Número de elementos no nulos.
-   `mean`: El promedio.
-   `std`: Desviación estándar.
-   `min` / `max`: Valores mínimos y máximos.
-   `25%`, `50%`, `75%`: Los cuartiles de la distribución.

**Incluir columnas de texto:**
Por defecto, `.describe()` omite las columnas tipo `object`. Para incluir un resumen de *todas* las columnas, puedes usar el argumento `include="all"`.

```python
# Incluye columnas numéricas y de texto (objetos)
df.describe(include="all")
```
Al incluir objetos, mostrará métricas diferentes para ellos:
-   `unique`: Cantidad de valores distintos.
-   `top`: El valor (texto) que más se repite.
-   `freq`: La cantidad de veces que aparece el valor `top`.
*(Nota: Verás múltiples valores `NaN` en la tabla porque, por ejemplo, no se puede calcular el promedio de una columna de texto, ni la frecuencia de un número continuo).*

## 3. Resumen Conciso del DataFrame (`df.info()`)
Otra función obligatoria para revisar el estado general del dataset.

```python
# Provee un resumen rápido y técnico del dataframe
df.info()
```
Te entregará información valiosa como:
-   El índice y tamaño del dataframe.
-   El tipo de dato (`Dtype`) de cada columna.
-   La **cantidad de valores no nulos** (útil para saber cuántos datos faltantes hay).
-   El uso total de memoria RAM del dataset.
