# Medidas para la Evaluación en la Muestra (In-Sample Evaluation)

Tras evaluar los modelos mediante gráficos (como rectas de regresión, residuos y curvas KDE), es necesario disponer de métricas numéricas objetivas para cuantificar con precisión qué tan bien se ajusta el modelo a los datos observados (*in-sample evaluation*).

Las dos métricas fundamentales más utilizadas en problemas de regresión son:
1. **Error Cuadrático Medio (MSE - Mean Squared Error)**
2. **R-cuadrado ($R^2$ - Coeficiente de Determinación)**

---

## 1. Error Cuadrático Medio (MSE - Mean Squared Error)

El **MSE** mide el promedio de los errores al cuadrado entre los valores reales observados y los valores predichos por el modelo.

### Cálculo Paso a Paso
1. **Diferencia (Error residual):** Para cada muestra $i$, restamos el valor real ($y_i$) y el valor pronosticado ($\hat{y}_i$).
   - *Ejemplo de la diapositiva:* Si el valor real es $y_1 = 150$ y el valor pronosticado por la recta es $\hat{y}_1 = 50$:
     $$e_1 = y_1 - \hat{y}_1 = 150 - 50 = 100$$
2. **Elevar al cuadrado:** Se eleva la diferencia al cuadrado para eliminar los signos negativos y penalizar con mayor peso los errores grandes:
   $$(e_1)^2 = (100)^2 = 10\,000$$
3. **Promedio sobre todas las muestras:** Se suman todos los errores cuadráticos y se divide entre el número total de muestras ($n$).

### Fórmula Matemática

$$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

### Interpretación del MSE
- Geométricamente, representa el **área promedio de los cuadrados** formados por las distancias verticales entre cada punto real y la línea de regresión.
- Mientras más pequeño sea el valor de MSE, más cerca estará la línea de regresión de los puntos reales y mejor será el ajuste del modelo.

### Implementación en Python con Scikit-Learn

```python
from sklearn.metrics import mean_squared_error

# mean_squared_error(valores_reales, valores_predichos)
mse_slr = mean_squared_error(df['price'], Y_predict_simple_fit)

print(mse_slr)
# Salida del ejemplo: 3163502.944639888
```

---

## 2. R-cuadrado ($R^2$ - Coeficiente de Determinación)

El **R-cuadrado ($R^2$)**, o coeficiente de determinación, es una medida normalizada que indica el **porcentaje de variación de la variable objetivo ($Y$) que es explicado por el modelo de regresión lineal**.

### ¿Cómo interpretarlo conceptualmente?
Consiste en comparar nuestro modelo de regresión frente a un **modelo base ingenuo**: la simple **media aritmética** de los puntos de datos ($\bar{y}$).
- Si la variable predictora $X$ es un buen predictor, nuestro modelo de regresión debería tener errores mucho menores que simplemente predecir la media para todos los casos.
- $R^2$ responde a la pregunta: *¿Qué tan cerca están nuestros datos reales del modelo estimado en comparación con el promedio básico?*

### Propiedades Clave de $R^2$
- **Rango típico:** Toma valores entre **0 y 1** (o entre 0% y 100%).
  - $R^2 = 1$ (100%): Ajuste perfecto; el modelo explica toda la variabilidad de los datos sin error.
  - $R^2 = 0$ (0%): El modelo no aporta información; se desempeña igual que usar la media de los datos.
- **Valores negativos:** En evaluación fuera de muestra (*out-of-sample*) o ante un sobreajuste severo (*overfitting*), $R^2$ puede resultar negativo, lo que indica que el modelo funciona incluso peor que la simple media.

---

## 3. Formulación Matemática de $R^2$ y Comparación de Áreas

La fórmula matemática formal del coeficiente de determinación compara el error del modelo frente al error de la línea de la media ($\bar{y}$):

$$R^2 = 1 - \frac{\text{MSE de la línea de regresión}}{\text{MSE de la media de los datos } (\bar{y})}$$

En términos de áreas geométricas de error:
- **Línea azul:** Representa la recta de regresión estimada por el modelo.
- **Cuadrados azules:** Representan el error cuadrático medio ($\text{MSE}$) respecto a la recta de regresión.
- **Línea roja horizontal:** Representa el promedio de los puntos ($\bar{y}$).
- **Cuadrados rojos:** Representan el error cuadrático medio ($\text{MSE}$) respecto a la media.

### Diagnóstico de Escenarios mediante el Cociente de Errores

| Escenario | Relación de Áreas (Azul vs Rojo) | Cociente $\frac{\text{MSE}(\text{recta})}{\text{MSE}(\bar{y})}$ | Valor de $R^2$ | Diagnóstico Técnico |
|---|---|---|---|---|
| **Buen Ajuste** | El área total de los cuadrados azules es **mucho menor** que la de los cuadrados rojos. | Numerador pequeño dividido entre denominador grande $\approx 0$. | **Cercano a 1** ($1 - 0 \approx 1$) | La recta reduce drásticamente el error en comparación con la media. El modelo es altamente predictivo. |
| **Mal Ajuste** | El área de los cuadrados azules es **casi idéntica** al área de los cuadrados rojos. | Numerador y denominador similares $\approx 1$. | **Cercano a 0** ($1 - 1 = 0$) | La recta no aporta ventaja predictiva alguna sobre predecir el simple promedio constante. |

#### Demostración del Caso de Mal Ajuste:

$$\frac{\text{MSE de la línea de regresión}}{\text{MSE de } \bar{y}} = \frac{\text{Área azul}}{\text{Área roja}} \approx 1$$

Sustituyendo en la ecuación general:

$$R^2 = 1 - 1 = 0$$

Cuando la relación de las áreas de error es cercana a uno, el modelo lineal tiene un rendimiento equivalente al de un modelo ingenuo que solo predice la media para cada observación.

---

## 4. Cálculo de $R^2$ en Python con Scikit-Learn (`lm.score`)

Para obtener el valor de $R^2$ de forma directa en Python, Scikit-Learn proporciona el método integrado `.score()` en cualquier estimador de regresión:

```python
# 1. Definir predictor y objetivo
X = df[['highway-mpg']]
Y = df['price']

# 2. Entrenar el modelo
lm.fit(X, Y)

# 3. Calcular el coeficiente de determinación R^2
r_cuadrado = lm.score(X, Y)

print(r_cuadrado)
# Salida: 0.49659118843391759
```

### Interpretación del Resultado:
- El valor obtenido es aproximadamente **$0.4966$** (o **$49.66\%$**).
- **Conclusión práctica:** Aproximadamente el **$49.66\%$ de la variación en el precio** del automóvil puede ser explicada por la variable independiente `highway-mpg` mediante este modelo de regresión lineal simple. El 50.34% restante de la variabilidad se debe a otros factores (peso, motor, marca, ruido estocástico).


