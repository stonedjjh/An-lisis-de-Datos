# Normalización de Datos

La **normalización de datos** es una técnica de preprocesamiento de datos muy importante. Se utiliza cuando las variables o características (features) de un conjunto de datos tienen rangos muy distintos y necesitamos que sean consistentes.

## ¿Por qué es importante normalizar?
Imagina que tienes un dataset con dos variables: **edad** (rango de 0 a 100) e **ingresos** (rango de 20,000 a 500,000). La variable "ingresos" es numéricamente unas 1,000 veces más grande que "edad". 

Al aplicar análisis estadísticos o algoritmos (como una regresión lineal), la naturaleza matemática de los datos sesgará el modelo, dándole automáticamente muchísimo más peso e influencia a los "ingresos" solo por tener valores más grandes, lo cual no significa que sea un predictor más importante que la edad. 

Normalizar permite una **comparación más justa** entre las diferentes características, garantizando que todas tengan un impacto equilibrado en el modelo analítico. Además, facilita el cálculo computacional.

---

## Métodos de Normalización y su implementación en Python (Pandas)

Existen múltiples enfoques para normalizar datos. Aquí presentamos los tres más comunes junto con su implementación en una línea de código usando Pandas:

### 1. Simple Feature Scaling (Escalado Simple de Características)
Consiste en dividir cada valor original por el valor máximo de esa característica. Los nuevos valores resultantes siempre estarán en un rango entre `0` y `1`.
- **Fórmula:** $X_{new} = \frac{X_{old}}{X_{max}}$

```python
# Dividir toda la columna por el valor máximo de la misma
df["length"] = df["length"] / df["length"].max()
```

### 2. Min-Max
A cada valor se le resta el valor mínimo de la característica y luego el resultado se divide por el rango total de la característica (el máximo menos el mínimo). Los valores resultantes también quedarán acotados entre `0` y `1`.
- **Fórmula:** $X_{new} = \frac{X_{old} - X_{min}}{X_{max} - X_{min}}$

```python
# Restar el mínimo y dividir por el rango (max - min)
df["length"] = (df["length"] - df["length"].min()) / (df["length"].max() - df["length"].min())
```

### 3. Z-score (Puntuación Estándar)
A cada valor se le resta el promedio o media ($\mu$) de la característica, y se divide por la desviación estándar ($\sigma$). Como resultado, los valores rondarán el `0` y típicamente se encontrarán en un rango entre `-3` y `+3` (aunque pueden ser ligeramente mayores o menores).
- **Fórmula:** $X_{new} = \frac{X_{old} - \mu}{\sigma}$

```python
# Restar la media (mean) y dividir por la desviación estándar (std)
df["length"] = (df["length"] - df["length"].mean()) / df["length"].std()
```
