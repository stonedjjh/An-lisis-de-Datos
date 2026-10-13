# Ficha del Módulo 4: Desarrollo de Modelos

**Curso:** Análisis de Datos con Python  
**Tema:** Hoja de trucos (Cheat Sheet) - Desarrollo de Modelos  

---

## Tabla Resumen de Procesos y Métodos

| Proceso | Descripción | Ejemplo de Código |
| :--- | :--- | :--- |
| **Crear objeto de Regresión Lineal** | Instanciar el estimador del modelo lineal desde `sklearn`. | ```python
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
``` |
| **Entrenar el modelo de Regresión Lineal** | Ajustar el modelo a los datos separando variables independientes ($X$) y objetivo ($Y$).<br>- **SLR (Simple):** Un solo predictor.<br>- **MLR (Múltiple):** Dos o más predictores. | ```python
# Para SLR: X = df[['attribute_1']]
# Para MLR:
X = df[['attribute_1', 'attribute_2']]
Y = df['target_attribute']

lr.fit(X, Y)
``` |
| **Generar predicciones** | Predecir los valores de salida ($\hat{Y}$) para una matriz de entrada $X$. | ```python
Y_hat = lr.predict(X)
``` |
| **Identificar pendiente e intercepto** | Obtener los parámetros de la recta o hiperplano: $\hat{Y} = \beta_0 + \beta_1 X_1 + \dots$<br>- Intercepto: $\beta_0$<br>- Pendientes: $\beta_1, \beta_2, \dots$ | ```python
# Pendientes (coeficientes)
coeff = lr.coef_

# Intercepto (ordenada al origen)
intercept = lr.intercept_
``` |
| **Gráfico de residuos** | Ajustar una regresión de $Y$ sobre $X$ y trazar los residuos. Un patrón no aleatorio sugiere que el modelo lineal no es el adecuado. | ```python
import seaborn as sns

sns.residplot(x=df['attribute_1'], y=df['attribute_2'])
``` |
| **Gráfico de distribución (KDE)** | Trazar la distribución continua estimada de los datos reales versus las predicciones para evaluar el ajuste global. | ```python
import seaborn as sns

# Versión moderna recomendada:
sns.kdeplot(df['attribute_name'], label='Real')

# Sintaxis clásica (hist=False):
# sns.distplot(df['attribute_name'], hist=False)
``` |
| **Regresión polinómica unidimensional** | Ajuste polinomial de orden $n$ sobre una única variable usando NumPy. | ```python
import numpy as np

# f contiene los coeficientes del polinomio de grado n
f = np.polyfit(x, y, n)

# p es el objeto función polinómica
p = np.poly1d(f)

# Predicciones
Y_hat = p(x)
``` |
| **Regresión polinómica multivariante** | Transformar una matriz multivariable $Z$ generando combinaciones polinómicas de grado menor o igual a $n$. | ```python
from sklearn.preprocessing import PolynomialFeatures

Z = df[['attribute_1', 'attribute_2']]
pr = PolynomialFeatures(degree=n)
Z_pr = pr.fit_transform(Z)
``` |
| **Canalización (Pipeline)** | Secuenciar pasos de preprocesamiento, escalado y ajuste de modelo de forma simplificada y automatizada. | ```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression

Input = [
    ('scale', StandardScaler()),
    ('polynomial', PolynomialFeatures(include_bias=False)),
    ('model', LinearRegression())
]

pipe = Pipeline(Input)
Z = Z.astype(float)
pipe.fit(Z, y)
ypipe = pipe.predict(Z)
``` |
| **Valor de $R^2$ (Coeficiente de determinación)** | Porcentaje de la variación de la variable objetivo que es explicado por el modelo:<br>**a.** Regresión lineal (SLR / MLR).<br>**b.** Regresión polinómica unidimensional. | ```python
# a. Con estimador de scikit-learn
R2_score = lr.score(X, Y)

# b. Con función polinomial de NumPy
from sklearn.metrics import r2_score
R2_score = r2_score(y, p(x))
``` |
| **Valor MSE (Error Cuadrático Medio)** | Promedio de los cuadrados de los errores entre los valores reales ($Y$) y los valores predichos ($\hat{Y}$). | ```python
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(Y, Yhat)
``` |

---

## Resumen de Interpretación y Criterios de Selección

1. **Mayor $R^2$:** Indica que el modelo explica una mayor proporción de la varianza en los datos.
2. **Menor MSE:** Indica que las predicciones del modelo tienen una menor distancia cuadrática respecto a los datos reales.
3. **Comparación entre modelos:**
   - Un $R^2$ más alto no siempre garantiza un mejor modelo si se produce sobreajuste (*overfitting*), especialmente con polinomios de grado elevado.
   - Siempre debe corroborarse la coherencia de las predicciones y examinar los gráficos de residuos y distribución KDE.
