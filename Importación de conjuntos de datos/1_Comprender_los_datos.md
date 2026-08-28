# Comprender los datos

Antes de comenzar a analizar o programar, es fundamental entender el contexto de la información con la que estamos trabajando. En este caso, analizaremos un conjunto de datos (dataset) abierto sobre **precios de autos usados**, originalmente recopilado por Jeffrey C. Schlimmer en 1985.

## El Formato CSV
El dataset se encuentra en formato **CSV** (Valores Separados por Comas). Es uno de los formatos más populares en ciencia de datos porque:
- Cada línea de texto representa una fila de datos (un registro o, en este caso, un auto).
- Los valores de cada característica están separados por comas.
- Es extremadamente ligero y fácil de importar en casi cualquier herramienta o lenguaje de programación (como Pandas en Python).

### ⚠️ Particularidad importante: Falta de Cabeceras (Headers)
Normalmente, la primera fila de un archivo CSV contiene los nombres de las columnas. Sin embargo, **en este dataset específico, la primera fila es directamente una fila de datos**, no contiene los nombres. Esto es crucial saberlo antes de programar, ya que significa que al momento de importar el archivo en Pandas, deberemos proporcionarle manualmente los nombres de las 26 columnas, de lo contrario Python creerá que el primer auto es el nombre de las columnas.

## Atributos Principales (Features / Predictores)
El dataset cuenta con 26 características en total. Algunas de las más interesantes son:

- **`symboling` (Nivel de riesgo):** Representa el nivel de riesgo del auto para las compañías de seguros. Un valor positivo como `+3` indica que es un vehículo riesgoso, mientras que un valor negativo como `-3` indica que es bastante seguro.
- **`normalized-losses` (Pérdidas normalizadas):** Representa el pago promedio de pérdida por vehículo asegurado al año. Este valor está "normalizado" o ponderado según la clasificación del tamaño del auto (dos puertas, deportivo, familiar, etc.). Sus valores oscilan entre 65 y 256.

## La Variable Objetivo (Target / Label)
El atributo número 26 es el **Precio (`price`)**. 

En machine learning y análisis predictivo, el `price` es nuestra **variable objetivo o etiqueta (label)**. Esto significa que la meta final de este proyecto es poder predecir el precio de un vehículo utilizando el resto de las 25 variables numéricas y categóricas (que actuarán como predictores).
