# Módulo 4: Desarrollo de Modelos

Este módulo aborda la formulación, entrenamiento, diagnóstico y optimización de modelos predictivos de Machine Learning y estadística aplicada. Partiendo de modelos lineales simples, se avanza hacia técnicas multivariables, evaluación visual diagnóstica, regresión polinómica y encadenamiento de flujos de trabajo mediante tuberías (*pipelines*).

---

## Objetivos de Aprendizaje

- Comprender la formulación matemática de la Regresión Lineal Simple (SLR) y la Regresión Lineal Múltiple (MLR).
- Ajustar estimadores lineales y extraer parámetros clave (`intercept_`, `coef_`) utilizando Scikit-Learn.
- Evaluar visualmente el rendimiento de los modelos con gráficos de regresión (`regplot`), gráficos de residuos (`residplot`) y curvas de densidad/distribución (`kdeplot`).
- Diagnosticar supuestos lineales: homocedasticidad frente a heterocedasticidad, y detección de patrones curvilíneos.
- Modelar relaciones no lineales mediante Regresión Polinómica unidimensional con NumPy (`polyfit`, `poly1d`) y multivariada con `PolynomialFeatures`.
- Implementar Tuberías (*Pipelines*) en Scikit-Learn para secuenciar la estandarización (`StandardScaler`), expansión polinómica y estimación lineal en un único flujo reproducible.

---

## Índice de Temas y Documentos

| # | Tema / Archivo | Resumen de Contenido |
|---|---|---|
| 1 | [1. Regresión Lineal Simple y Múltiple](./1_Regresi%C3%B3n_lineal_y_regresi%C3%B3n_lineal_m%C3%BAltiple.md) | Fundamentos de SLR y MLR, interpretación de la intersección ($b_0$) y coeficientes ($b_1, \dots, b_n$), espacio geométrico 3D, concepto de ruido, y entrenamiento con `LinearRegression` en Scikit-Learn. |
| 2 | [2. Evaluación de Modelos Mediante Visualización](./2._Evaluaci%C3%B3n_de_modelos_mediante_visualizaci%C3%B3n.md) | Diagnóstico visual con Seaborn: gráficos de regresión (`regplot`), análisis de residuos (`residplot`) con detección de curvatura y heterocedasticidad, y gráficos de distribución comparativos (`kdeplot`) para SLR frente a MLR. |
| 3 | [3. Regresión Polinómica y Tuberías](./3_Regresi%C3%B3n_polin%C3%B3mica_y_tuber%C3%ADas.md) | Modelado curvilíneo con polinomios de grado 2, 3 y superior; uso de `np.polyfit` y `np.poly1d`; expansión multidimensional con `PolynomialFeatures`; estandarización simultánea con `StandardScaler`; y construcción de flujos completos con `Pipeline`. |
| 4 | [4. Gráficos KDE para Evaluación del Modelo](./4_Gr%C3%A1ficos_de_estimaci%C3%B3n_de_la_densidad_del_n%C3%BAcleo_%28KDE%29_para_la_Evaluaci%C3%B3n_del_modelo.md) | Estimación de la función de densidad de probabilidad (PDF) con `sns.kdeplot()`, ventajas frente a histogramas, código reproducible con `train_test_split`, e interpretación diagnóstica de solapamiento, modas y dispersión. |
| 5 | [5. Medidas para la Evaluación en la Muestra](./5_Medidas_para_la_evaluaci%C3%B3n_en_la_muestra.md) | Métricas numéricas de bondad de ajuste: Error Cuadrático Medio (`mean_squared_error`), Coeficiente de Determinación ($R^2$) mediante `.score()`, comparación geométrica de áreas de error frente a la media, e interpretación porcentual de la varianza explicada. |
| 6 | [6. Predicción y Toma de Decisiones](./6_Predicci%C3%B3n_y_toma_de_decisiones.md) | Criterios integrales de selección de modelos: validación de sentido común, detección de predicciones negativas con `np.arange`, diagnóstico visual combinado, escala de $R^2$, y por qué un menor MSE en la muestra no siempre implica un mejor modelo (sesgo de sobreajuste). |
| 7 | [Resumen de la Lección](./Resumen_de_la_lecci%C3%B3n.md) | Síntesis conceptual exhaustiva de todo el módulo: fundamentos lineales, diagnóstico visual de residuos y KDE, transformación polinómica, pipelines, métricas cuantitativas (MSE, $R^2$) y directrices de toma de decisiones. |

---

## Métodos y Sintaxis Clave

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

# 1. Regresión Lineal Múltiple
Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
lm = LinearRegression()
lm.fit(Z, df['price'])
yhat = lm.predict(Z)

# 2. Regresión Polinómica 1D con NumPy
f = np.polyfit(df['highway-mpg'], df['price'], 3)
p = np.poly1d(f)

# 3. Flujo Integrado con Pipeline
flujo = [
    ('scale', StandardScaler()),
    ('polynomial', PolynomialFeatures(degree=2, include_bias=False)),
    ('model', LinearRegression())
]
pipe = Pipeline(flujo)
pipe.fit(Z, df['price'])
yhat_pipe = pipe.predict(Z)
```
