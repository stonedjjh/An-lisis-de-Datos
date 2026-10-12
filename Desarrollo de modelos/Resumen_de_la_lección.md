# Resumen de la Lección: Desarrollo de Modelos

Este documento sintetiza los conceptos, herramientas y metodologías fundamentales estudiadas a lo largo de este módulo de desarrollo, evaluación y selección de modelos predictivos.

---

## 1. Fundamentos de Regresión

- **Regresión Lineal Simple (SLR):** Modela la relación directa entre una única variable independiente predictora ($X$) y una variable objetivo continua ($Y$) mediante una recta: $\hat{Y} = b_0 + b_1 X$.
- **Regresión Lineal Múltiple (MLR):** Extiende el análisis para explicar una variable objetivo continua ($Y$) a partir de dos o más variables predictoras independientes ($X_1, X_2, \dots, X_n$) mediante un plano o hiperplano: $\hat{Y} = b_0 + b_1 X_1 + \dots + b_n X_n$.

---

## 2. Diagnóstico y Evaluación Mediante Visualización

- **Gráficos de Regresión (`sns.regplot`):** Permiten estimar visualmente la fuerza, dirección (positiva o negativa) y grado de linealidad de la relación entre el predictor y el objetivo.
- **Gráficos de Residuos (`sns.residplot`):**
  - **Ajuste lineal adecuado:** Los residuos deben tener media cero, distribuirse aleatoriamente alrededor del eje horizontal y presentar varianza uniforme (homocedasticidad).
  - **Ajuste lineal inadecuado:** La presencia de una curvatura visible (forma de U / parábola) o varianza cambiante en abanico (heterocedasticidad) indica que el supuesto lineal no se cumple y se requiere un modelo no lineal o polinómico.
- **Gráficos de Distribución / KDE (`sns.kdeplot`):** Herramienta definitiva para modelos con múltiples predictores (MLR), donde los gráficos 2D no son aplicables. Permite comparar la curva de densidad de los valores reales frente a los valores predichos, identificando rangos de valores donde el modelo pierde precisión.

---

## 3. Regresión Polinómica y Transformación de Características

- **Naturaleza Curvilínea:** Permite ajustar curvas complejas elevando las variables predictoras a potencias superiores ($X^2, X^3, \dots, X^n$). Aunque la curva geométrica no es recta, los parámetros ($b_i$) se estiman linealmente.
- **NumPy para 1D (`np.polyfit` y `np.poly1d`):** `np.polyfit` calcula los coeficientes numéricos del polinomio por mínimos cuadrados, y `np.poly1d` construye el objeto función para evaluar y visualizar la ecuación simbólica.
- **Scikit-Learn para Dimensiones Múltiples:** La clase `PolynomialFeatures` de `sklearn.preprocessing` permite generar términos polinómicos y productos cruzados de interacción entre múltiples características.
- **Normalización Simultánea:** El módulo `StandardScaler` estandariza múltiples columnas restando la media y dividiendo por la desviación estándar, evitando que variables con escalas grandes dominen el ajuste.

---

## 4. Tuberías (Pipelines)

- **Automatización del Flujo:** La clase `Pipeline` de Scikit-Learn permite encadenar secuencialmente pasos de preprocesamiento (normalización con `StandardScaler`, expansión polinómica con `PolynomialFeatures`) y el estimador final (`LinearRegression`).
- **Ventajas:**
  - Código compacto, legible y mantenible.
  - Prevención de fugas de datos (*data leakage*).
  - Ejecución integral mediante llamadas únicas a `.fit()` y `.predict()`.

---

## 5. Medidas Numéricas para la Evaluación en la Muestra

- **Error Cuadrático Medio (MSE / ECM):**
  - Mide la media aritmética de los cuadrados de las diferencias entre los valores reales y los pronosticados: $\text{MSE} = \frac{1}{n}\sum(y_i - \hat{y}_i)^2$.
  - Es la medida numérica más intuitiva de cercanía: a menor MSE, menor error promedio.
  - Se calcula con `mean_squared_error(y_real, y_pred)` de `sklearn.metrics`.
- **Coeficiente de Determinación ($R^2$):**
  - Mide la proporción de la varianza en la variable dependiente que es explicada por las variables independientes: $R^2 = 1 - \frac{\text{MSE}(\text{modelo})}{\text{MSE}(\bar{y})}$.
  - Se calcula directamente con el método `.score(X, y)` del estimador.
  - Un valor cercano a $1$ con un MSE bajo indica un buen ajuste; un valor cercano a $0$ indica que el modelo no supera al promedio constante.
  - Un valor negativo de $R^2$ puede ser síntoma de sobreajuste severo (*overfitting*).
  - El umbral aceptable de $R^2$ depende del área de aplicación (en ciencias físicas se exige $> 0.90$, mientras que en ciencias sociales o finanzas valores $\ge 0.10$ o $0.30$ pueden ser útiles).

---

## 6. Toma de Decisiones y Selección de Modelos

- **Regla del Sentido Común:** Comprobar siempre que las predicciones puntuales sean físicamente posibles (por ejemplo, evitar precios negativos generados por extrapolación lineal en rangos irreales).
- **La Trampa del MSE en Modelos Complejos:** Un menor MSE o un mayor $R^2$ en la muestra de entrenamiento **no garantiza** un mejor modelo. Los modelos MLR y las regresiones polinómicas de alto grado casi siempre reducen el MSE en los datos de entrenamiento porque tienen más parámetros para memorizar las muestras, lo cual puede derivar en sobreajuste.
- **Criterio de Elección Definitivo:** Integrar la validación visual de residuos y densidades, la consistencia de los coeficientes en el dominio de negocio, y la evaluación con datos no vistos (validación cruzada y evaluación fuera de muestra).
