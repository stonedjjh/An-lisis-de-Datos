# Regresión Lineal Simple y Regresión Lineal Múltiple

En el desarrollo de modelos predictivos, la regresión lineal es uno de los métodos estadísticos y de Machine Learning fundamentales. Su propósito es estimar y cuantificar la relación entre una o más variables predictoras independientes y una variable objetivo continua.

---

## 1. Regresión Lineal Simple (SLR - Simple Linear Regression)

La Regresión Lineal Simple permite modelar la relación matemática entre **dos variables**:
- **Variable Independiente ($X$):** Predictor o característica utilizada para realizar la predicción.
- **Variable Dependiente ($Y$):** Objetivo o etiqueta (*target / label*) que deseamos predecir.

### Ecuación Matemática

$$Y = b_0 + b_1 \cdot X$$

Donde:
- **$b_0$ (Intersección / Intercept):** El valor de $Y$ cuando $X = 0$.
- **$b_1$ (Pendiente / Slope):** La tasa de cambio en $Y$ por cada unidad de incremento en $X$.

Una vez ajustado el modelo, las predicciones se representan mediante $\hat{Y}$ (*Y-hat*), indicando que es un valor estimado:

$$\hat{Y} = b_0 + b_1 \cdot X$$

---

## 2. Ajuste del Modelo y Concepto de Ruido

### Puntos de Entrenamiento y Estimación de Parámetros
Para encontrar los valores óptimos de $b_0$ y $b_1$, el algoritmo toma los puntos reales del conjunto de datos (puntos de entrenamiento) y traza la recta que mejor se ajuste a ellos.

- Las variables predictoras se estructuran en una matriz o DataFrame $X$ (donde cada fila representa una muestra).
- La variable objetivo se estructura en un vector o Serie $y$.

### El Ruido (Incertidumbre)
En problemas reales, múltiples factores no medidos (marca, antigüedad, estado del vehículo) influyen en el resultado final. El modelo asume que existe un componente aleatorio agregado a la línea llamado **ruido**:
- En su mayoría, los valores de ruido son pequeños y cercanos a cero.
- En ocasiones se producen desviaciones mayores, lo que explica por qué el valor predicho ($\hat{Y}$) no coincide exactamente con el valor real observado ($Y$).

---

## 3. Implementación de SLR en Python con Scikit-Learn

Para ajustar un modelo de regresión lineal simple en Python utilizamos la biblioteca `scikit-learn`:

### Paso 1: Importar y crear el estimador

```python
from sklearn.linear_model import LinearRegression

# Crear el objeto de regresión lineal
lm = LinearRegression()
```

### Paso 2: Definir variables y ajustar el modelo (`fit`)

```python
# X debe ser un DataFrame o matriz bidimensional
X = df[['highway-mpg']]
# Y es la variable objetivo
Y = df['price']

# Ajustar el modelo para calcular b0 y b1
lm.fit(X, Y)
```

### Paso 3: Generar predicciones (`predict`)

```python
# Realizar predicciones sobre los datos de entrada
Yhat = lm.predict(X)
```

La salida `Yhat` es un arreglo unidimensional con la misma cantidad de filas que la entrada `X`.

### Paso 4: Consultar parámetros calculados

Los parámetros calculados tras el ajuste quedan almacenados como atributos del objeto `lm`:

- **Intersección ($b_0$):** `lm.intercept_`
- **Pendiente / Coeficiente ($b_1$):** `lm.coef_`

#### Ejemplo con Datos de Automóviles:
- Intersección ($b_0$): `38423.305858`
- Coeficiente ($b_1$): `-821.73337832`

**Ecuación estimada resultante:**

$$\text{Price} = 38423.31 - 821.73 \cdot \text{highway-mpg}$$

Esta relación indica que, en promedio, por cada milla por galón adicional en carretera, el precio estimado del automóvil disminuye en $821.73.

---

## 4. Regresión Lineal Múltiple (MLR - Multiple Linear Regression)

Cuando una sola variable predictora no es suficiente para explicar la variabilidad del objetivo, se utiliza la **Regresión Lineal Múltiple**. Este método modela la relación entre:
- **Una variable objetivo continua ($Y$)**
- **Dos o más variables predictoras ($X_1, X_2, \dots, X_n$)**

### Ecuación Matemática

$$\hat{Y} = b_0 + b_1 X_1 + b_2 X_2 + b_3 X_3 + \dots + b_n X_n$$

Donde:
- **$b_0$:** Intersección del plano o hiperplano cuando todos los predictores valen 0.
- **$b_1, b_2, \dots, b_n$:** Coeficientes de regresión o parámetros asociados a cada predictor $X_1, X_2, \dots, X_n$. Cada coeficiente representa el cambio esperado en $\hat{Y}$ por cada unidad de cambio en su variable predictora correspondiente, manteniendo todas las demás constantes.

### Interpretación Geométrica (Visualización con 2 Predictores)

Cuando trabajamos con dos variables predictoras ($X_1$ y $X_2$), la relación se puede visualizar en un espacio tridimensional:
- El plano horizontal (ejes $X_1$ y $X_2$) representa las combinaciones de las variables predictoras (plano 2D).
- El eje vertical representa el valor estimado $\hat{Y}$, cuya altura es proporcional al resultado del cálculo.

#### Ejemplo Numérico de Mapeo 3D:

Dada la ecuación:

$$\hat{Y} = 1 + 2X_1 + 3X_2$$

| Muestra ($n$) | $X_1$ | $X_2$ | Coordenada en Base $(X_1, X_2)$ | Cálculo de $\hat{Y}$ | Altura ($\hat{Y}$) |
|---|---|---|---|---|---|
| 1 | 0 | 0 | $(0, 0)$ | $1 + 2(0) + 3(0)$ | **1** |
| 2 | 0 | 2 | $(0, 2)$ | $1 + 2(0) + 3(2)$ | **6** |
| 3 | 1 | 0 | $(1, 0)$ | $1 + 2(1) + 3(0)$ | **2** |
| 4 | 3 | 2 | $(3, 2)$ | $1 + 2(3) + 3(2)$ | **13** |

En lugar de trazar una recta (como en SLR), con dos predictores el modelo genera un **plano bidimensional** en el espacio 3D. Con más de dos predictores ($n \ge 3$), el modelo define un **hiperplano multidimensional**.

---

## 5. Implementación de MLR en Python con Scikit-Learn

El flujo de trabajo en Python para regresión múltiple es idéntico al de regresión simple, con la diferencia de que la matriz de entrada contiene múltiples columnas predictoras.

### Paso 1: Extraer múltiples predictores

Seleccionamos un subconjunto de características del DataFrame original y las almacenamos en una variable (por ejemplo, $Z$):

```python
# Definir el conjunto de 4 variables predictoras
Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
```

### Paso 2: Entrenar el modelo (`fit`)

Utilizamos el mismo estimador `LinearRegression` pasando la matriz multidimensional $Z$ y la variable objetivo:

```python
# Ajustar el modelo con múltiples variables independientes
lm.fit(Z, df['price'])
```

### Paso 3: Generar predicciones (`predict`)

```python
# Realizar predicciones basadas en la matriz de 4 predictores
Yhat = lm.predict(Z)
```

- **Entrada:** Un DataFrame o matriz bidimensional de dimensiones $(m \times 4)$, donde $m$ es el número de muestras (filas) y 4 es el número de predictores.
- **Salida:** Un arreglo unidimensional de tamaño $m$ con las predicciones calculadas ($\hat{Y}$).

### Paso 4: Obtener parámetros del modelo estimado

Una vez entrenado el modelo, consultamos los atributos calculados por Scikit-Learn:

#### 1. Intersección ($b_0$)
```python
lm.intercept_
# Salida: -15678.742628061467
```

#### 2. Coeficientes ($b_1, b_2, b_3, b_4$)
```python
lm.coef_
# Salida: array([52.65851272, 4.69878948, 81.95906216, 33.58258185])
```

Los coeficientes corresponden ordenadamente a las 4 variables de entrada definidas en $Z$:
- $b_1 = 52.66 \rightarrow$ `horsepower` (caballos de fuerza)
- $b_2 = 4.70 \rightarrow$ `curb-weight` (peso al vacío)
- $b_3 = 81.96 \rightarrow$ `engine-size` (tamaño del motor)
- $b_4 = 33.58 \rightarrow$ `highway-mpg` (millas por galón en carretera)

---

### Ecuación Final del Modelo Estimado (MLR)

Sustituyendo los parámetros numéricos obtenidos en la fórmula general:

$$\hat{Y} = b_0 + b_1 X_1 + b_2 X_2 + b_3 X_3 + b_4 X_4$$

Obtenemos la ecuación predictiva concreta para el precio de los automóviles:

$$\text{Price} = -15678.74 + 52.66 \cdot \text{horsepower} + 4.70 \cdot \text{curb-weight} + 81.96 \cdot \text{engine-size} + 33.58 \cdot \text{highway-mpg}$$

#### Interpretación de los coeficientes:
- **Intersección ($-15678.74$):** Constante base del modelo (ajuste matemático cuando los predictores son 0).
- **`horsepower` ($+52.66$):** Por cada caballo de fuerza adicional, el precio estimado sube aproximadamente \$52.66 (manteniendo fijas las demás variables).
- **`curb-weight` ($+4.70$):** Por cada libra adicional de peso, el precio aumenta alrededor de \$4.70.
- **`engine-size` ($+81.96$):** Cada incremento unitario en el tamaño del motor incrementa el precio en \$81.96.
- **`highway-mpg` ($+33.58$):** En este modelo multivariable, tras controlar el efecto conjunto de potencia, peso y motor, las millas por galón en carretera aportan un valor positivo de \$33.58 por unidad.


