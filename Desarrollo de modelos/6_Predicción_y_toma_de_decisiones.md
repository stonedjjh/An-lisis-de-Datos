# Predicción y Toma de Decisiones

El paso final en el ciclo de vida del desarrollo de modelos consiste en la **toma de decisiones**: determinar si el modelo entrenado es adecuado, confiable y aplicable en el mundo real. 

Para validar un modelo no basta con observar una métrica aislada; se requiere evaluar una combinación equilibrada de cuatro pilares:
1. **Sentido común de las predicciones:** ¿Los valores predichos son lógicos y realistas en el contexto del negocio?
2. **Visualización:** ¿Los gráficos de regresión, residuos y distribución confirman que se cumplen los supuestos?
3. **Medidas numéricas de evaluación:** ¿Los valores de MSE y $R^2$ son competitivos?
4. **Comparación entre diferentes modelos:** ¿Un modelo lineal simple, múltiple o polinómico ofrece el mejor balance entre precisión y complejidad?

---

## 1. Validación de Sentido Común: ¿Tienen Sentido los Valores Predichos?

Antes de desplegar cualquier estimador, debemos comprobar empíricamente qué predicciones produce para casos puntuales y evaluar la coherencia de sus parámetros.

### Ejemplo 1: Predicción en Rango Típico
Partiendo del modelo de regresión lineal simple:

$$\text{Price} = 38423.31 - 821.73 \cdot \text{highway-mpg}$$

Si deseamos predecir el precio para un vehículo con **$30\text{ mpg}$** en carretera:

```python
import numpy as np

# Entrada bidimensional (1 muestra, 1 característica)
nuevo_auto = np.array(30.0).reshape(-1, 1)

precio_predicho = lm.predict(nuevo_auto)
print(precio_predicho)
# Salida: $13771.30
```

- **Evaluación lógica:** El valor resultante (\$13,771.30) es positivo, coherente con el mercado de autos usados y consistente con la tendencia.
- **Evaluación de coeficientes:** Al inspeccionar `lm.coef_` ($-821.73$), observamos que por cada milla por galón adicional en carretera, el precio desciende aproximadamente \$821 dólares, lo cual es razonable dado que vehículos más económicos o compactos suelen ser menos costosos que vehículos deportivos o de gran tamaño.

---

## 2. Detección de Incoherencias: Rango de Validez del Modelo

Un error frecuente ocurre al **extrapolar el modelo fuera del dominio de datos de entrenamiento**.

### Prueba de Estrés con `np.arange`
Si evaluamos el comportamiento del modelo en un rango extendido de 1 a 100 millas por galón:

```python
import numpy as np

# Generar secuencia de 1 a 100 con paso de 1
# np.arange(inicio, fin_exclusivo, paso)
new_input = np.arange(1, 101, 1).reshape(-1, 1)

# Predecir sobre todo el rango
yhat = lm.predict(new_input)
```

### Análisis del Resultado Numérico:
- Para valores superiores a aproximadamente $47\text{ mpg}$, la recta cruza el eje horizontal y **comienza a predecir precios negativos** (alcanzando hasta $-\$42,928$ para $100\text{ mpg}$).
- **¿Por qué ocurre esto?**
  1. **Valores no realistas en la práctica:** La inmensa mayoría de automóviles convencionales de combustión no alcanzan 60–100 mpg en carretera.
  2. **Ausencia de datos:** El conjunto de entrenamiento no posee registros en ese rango extremo.
  3. **Límite de la suposición lineal:** Una recta no puede doblar; seguirá descendiendo indefinidamente hacia el infinito negativo a menos que se restrinja el dominio o se use un modelo no lineal/polinómico.
- **Conclusión técnica:** El modelo es válido **únicamente dentro del rango operativo de los datos observados** (aproximadamente entre $15$ y $50\text{ mpg}$). Fuera de ese rango, las predicciones carecen de validez física.

---

## 3. Evaluación Visual Diagnóstica

La visualización gráfica es el primer filtro para detectar problemas estructurales antes de confiar en una ecuación:

### 1. Gráfica de Regresión
- Permite confirmar si la variable independiente ejerce una influencia real y en qué dirección (por ejemplo, pendiente descendente del precio al aumentar `highway-mpg`).
- Señala si los datos presentan una curvatura natural que una línea recta no puede seguir.

### 2. Gráfica de Residuos
- Si los residuos exhiben una **curvatura visible** (patrón en U o parábola), confirman que el supuesto lineal es incorrecto y sugieren la necesidad de un modelo polinómico o no lineal.

### 3. Gráfica de Distribución (para Regresión Múltiple)
- Permite comparar simultáneamente la densidad real de los precios frente a la densidad predicha.
- Señala rangos específicos de falla: por ejemplo, si el modelo lineal comete errores notables en precios altos (\$30,000 a \$50,000), indica que se requieren más datos en ese segmento o términos de orden superior.

---

## 4. Medidas Numéricas: Impacto Visual del MSE

El **Error Cuadrático Medio (MSE)** es la medida numérica más intuitiva de cercanía:
- **MSE Bajo (ej. $3.495$ o $3.652$):** Los puntos reales observados se encuentran estrechamente agrupados alrededor de la recta de regresión ajustada.
- **MSE Alto (ej. $12.870$ o superior):** Los puntos reales se dispersan y se alejan considerablemente de la recta pronosticada.

A medida que el valor de MSE aumenta, los puntos objetivos se alejan de la línea ajustada.

---

## 5. Medidas Numéricas: Escala Visual de $R^2$

El coeficiente $R^2$ refleja qué tan evidente es la relación lineal frente a la dispersión aleatoria:

| Valor de $R^2$ | Comportamiento Visual de los Datos | Interpretación |
|---|---|---|
| **$R^2 = 0.9986$** | Puntos rojos prácticamente pegados a la línea azul ajustada. | Ajuste casi perfecto; la relación lineal explica casi la totalidad de la varianza. |
| **$R^2 = 0.9226$** | Ligera dispersión alrededor de la recta, pero la alineación es sólida. | Fuerte relación lineal con ruido bajo. |
| **$R^2 = 0.8060$** | Mayor dispersión de puntos ("nube" más ancha), aunque la tendencia ascendente es indiscutible. | Buena relación lineal en presencia de variabilidad moderada. |
| **$R^2 = 0.6181$** | Puntos notablemente dispersos dentro de una banda ancha. | La función lineal es más difícil de apreciar a simple vista, pero estadísticamente los datos crecen con la variable independiente. |

*Nota sobre umbrales de aceptación:* El valor aceptable de $R^2$ depende del campo de estudio. En ciencias físicas o ingeniería se exigen valores superiores a $0.90$, mientras que en ciencias sociales, finanzas o comportamiento del consumidor valores de $R^2 \ge 0.10$ o $0.30$ pueden considerarse informativos debido a la alta variabilidad humana.

---

## 6. Comparación entre Modelos: SLR, MLR y Regresión Polinómica

Una pregunta fundamental en la toma de decisiones es: **¿Un MSE más bajo (o un $R^2$ más alto) implica siempre que un modelo es mejor?**

La respuesta es: **No necesariamente.**

### La Trampa del Sobreajuste en la Muestra (*In-Sample Bias*)
1. **MLR frente a SLR:** El MSE de un modelo de regresión lineal múltiple casi siempre será **menor** que el de un modelo simple, y su $R^2$ será **mayor**. Esto ocurre porque al añadir variables adicionales, el algoritmo encuentra más grados de libertad matemáticos para ajustarse a los errores específicos de los datos de entrenamiento.
2. **Regresión Polinómica:** Al elevar características a potencias superiores ($X^2, X^3, \dots, X^n$), el modelo genera curvas complejas que reducen aún más el MSE en la muestra de entrenamiento.

### Regla de Decisión Final
- Que un modelo complejo tenga un MSE menor sobre los datos de entrenamiento **no garantiza que vaya a predecir bien sobre datos nuevos y nunca vistos**.
- Un modelo excesivamente complejo puede memorizar el ruido estocástico en lugar del patrón real (sobreajuste / *overfitting*).
- **Criterio equilibrado:** La elección final del modelo debe basarse en la combinación de:
  - Sentido común de los coeficientes y las predicciones en el dominio real.
  - Ausencia de patrones en los gráficos de residuos.
  - Validación cruzada y evaluación fuera de la muestra (*out-of-sample evaluation*), técnica que se estudiará en el siguiente módulo.


