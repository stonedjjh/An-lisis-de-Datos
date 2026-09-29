import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# 1. Cargar el conjunto de datos
nombre_archivo = "automobileEDA.csv"
df = pd.read_csv(nombre_archivo, header=0)

# Ver las primeras 5 filas del DataFrame con df.head()
print("Las primeras 5 filas del dataframe son:\n", df.head())

'''
Análisis de Patrones en Características Individuales Usando Visualización

¿Cómo elegir el método de visualización adecuado?
Al visualizar variables individuales, es importante entender primero con qué tipo de dato estamos tratando.
Esto nos ayudará a elegir la visualización correcta para cada variable.
'''

print("Tipos de datos en el DataFrame:\n", df.dtypes)

'''
Pregunta #1:
¿Cuál es el tipo de dato de la columna "peak-rpm"?
'''
print("El tipo de dato de df['peak-rpm'] es:", df['peak-rpm'].dtypes)

# Por ejemplo, podemos calcular la correlación entre variables numéricas ("int64" o "float64") usando el método corr():
df_numerico = df.select_dtypes(include=['float64', 'int64'])
print("La matriz de correlación entre variables numéricas es:\n", df_numerico.corr())

'''
Pregunta #2:
Encuentra la correlación entre las siguientes columnas: 'bore', 'stroke', 'compression-ratio' y 'horsepower'.
Pista: selecciona las columnas con la sintaxis: df[['bore','stroke','compression-ratio','horsepower']]
'''
print("Correlación entre 'bore', 'stroke', 'compression-ratio' y 'horsepower':\n", 
      df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr())

'''
Variables Numéricas Continuas:
Son variables que pueden tomar cualquier valor dentro de un rango determinado. Suelen ser de tipo int64 o float64.
Una excelente manera de visualizarlas es mediante diagramas de dispersión (scatter plots) con una línea de ajuste.

Para entender la relación (lineal) entre una variable individual y el precio (variable objetivo), podemos usar regplot de Seaborn,
el cual dibuja el diagrama de dispersión junto con la recta de regresión ajustada.
'''

# Relación Lineal Positiva:
# Veamos el gráfico de dispersión entre el tamaño del motor ("engine-size") y el precio ("price").
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)
plt.title("Tamaño del Motor vs Precio")
plt.xlabel("Tamaño del Motor (Engine Size)")
plt.ylabel("Precio")
plt.show()

'''
Conclusión:
A medida que el tamaño del motor aumenta, el precio sube: esto indica una correlación directa y positiva entre ambas variables.
El tamaño del motor parece ser un excelente predictor del precio, ya que la recta de regresión es casi una diagonal perfecta.
'''
print("La correlación entre engine-size y price es:", df['engine-size'].corr(df['price']))

# Relación Lineal Negativa:
# Las millas por galón en autopista ("highway-mpg") como predictor potencial del precio.
sns.regplot(x="highway-mpg", y="price", data=df)
plt.title("Millas por Galón en Autopista vs Precio")
plt.xlabel("Millas por Galón en Autopista (Highway MPG)")
plt.ylabel("Precio")
plt.show()

'''
Conclusión:
A medida que aumenta el highway-mpg, el precio disminuye: esto indica una relación inversa/negativa.
highway-mpg podría ser un buen predictor del precio.
'''
print("La correlación entre highway-mpg y price es:", df['highway-mpg'].corr(df['price']))

'''
Relación Lineal Débil:
Veamos si "peak-rpm" (revoluciones máximas por minuto) es un buen predictor del precio.
'''
sns.regplot(x="peak-rpm", y="price", data=df)
plt.title("Peak RPM vs Precio")
plt.xlabel("Revoluciones Máximas (Peak RPM)")
plt.ylabel("Precio")
plt.show()

'''
Conclusión:
Peak-rpm no parece un buen predictor del precio en lo absoluto. La recta de regresión es casi horizontal.
Además, los puntos de datos están muy dispersos y alejados de la recta, mostrando mucha variabilidad.
'''
print("La correlación entre peak-rpm y price es:", df['peak-rpm'].corr(df['price']))

'''
Pregunta 3 a):
Encuentra la correlación entre x="stroke" (carrera del pistón) e y="price".
'''
print("La correlación entre stroke y price es:\n", df[['stroke', 'price']].corr())

'''
Pregunta 3 b):
Dado el resultado de la correlación entre "price" y "stroke", ¿esperas una relación lineal?
Verifiquémoslo con regplot().
'''
sns.regplot(x="stroke", y="price", data=df)
plt.title("Stroke vs Precio")
plt.xlabel("Carrera del Pistón (Stroke)")
plt.ylabel("Precio")
plt.show()

'''
Variables Categóricas:
Son variables que describen una característica y pertenecen a un grupo cerrado de categorías.
Pueden tener tipo 'object' (strings) o a veces códigos numéricos ('int64').
Una excelente manera de visualizar variables categóricas frente a una variable numérica es con Diagramas de Caja y Bigotes (Boxplots).
'''

# Relación entre "body-style" (estilo de carrocería) y precio:
sns.boxplot(x="body-style", y="price", data=df)
plt.title("Estilo de Carrocería vs Precio")
plt.xlabel("Estilo de Carrocería (Body Style)")
plt.ylabel("Precio")
plt.show()

'''
Conclusión:
Vemos que las distribuciones de precio entre las diferentes categorías de estilo de carrocería se solapan significativamente;
por tanto, body-style no sería un predictor contundente del precio.
'''

# Relación entre "engine-location" (ubicación del motor) y precio:
sns.boxplot(x="engine-location", y="price", data=df)
plt.title("Ubicación del Motor vs Precio")
plt.xlabel("Ubicación del Motor (Frontal vs Trasera)")
plt.ylabel("Precio")
plt.show()

'''
Conclusión:
Aquí vemos que la distribución de precios entre las dos categorías (frontal y trasera) es claramente distinta.
La ubicación del motor parece ser un predictor clave.
'''

# Relación entre "drive-wheels" (tipo de tracción) y precio:
sns.boxplot(x="drive-wheels", y="price", data=df)
plt.title("Tipo de Tracción vs Precio")
plt.xlabel("Tipo de Tracción (Drive Wheels)")
plt.ylabel("Precio")
plt.show()

'''
Conclusión:
La distribución de precios difiere claramente según el tipo de tracción (delantera 'fwd', trasera 'rwd', cuatro ruedas '4wd').
Por lo tanto, 'drive-wheels' es un predictor potencial del precio.
'''

'''
Análisis Estadístico Descriptivo:
La función describe() calcula automáticamente estadísticas básicas de todas las variables numéricas continuas,
omitiendo automáticamente los valores NaN.

Muestra:
- Conteo (count)
- Media (mean)
- Desviación estándar (std)
- Valor mínimo (min)
- Rango intercuartílico (25%, 50% [mediana] y 75%)
- Valor máximo (max)
'''
print("Resumen estadístico de variables numéricas:\n", df.describe())

# Para incluir variables de tipo objeto (categóricas) usamos include=['object']:
print("Resumen estadístico de variables categóricas:\n", df.describe(include=['object']))

'''
Conteo de Valores (Value Counts):
Es útil para saber cuántas unidades tenemos de cada categoría.
Solo funciona sobre Series de Pandas (una sola columna: df['columna']), no sobre DataFrames completos.
'''
print("Conteo de valores para drive-wheels:\n", df['drive-wheels'].value_counts())

# Convertimos la Serie a DataFrame y renombramos columnas para mayor claridad:
conteo_traccion = df['drive-wheels'].value_counts().to_frame()
conteo_traccion.reset_index(inplace=True)
conteo_traccion.rename(columns={'drive-wheels': 'tipo_traccion', 'count': 'cantidad'}, inplace=True)
print("DataFrame formateado de conteos de tracción:\n", conteo_traccion)

# Repitamos el conteo con 'engine-location':
conteo_ubicacion_motor = df['engine-location'].value_counts().to_frame()
print("Conteo de valores de ubicación del motor:\n", conteo_ubicacion_motor)

'''
Conclusión sobre Engine Location:
Aunque en el boxplot se veían muy separados, al mirar los conteos vemos que solo hay 3 autos con motor trasero y 198 con motor delantero.
La muestra está muy sesgada (desbalanceada); por tanto, no es seguro extraer conclusiones estadísticas firmes con tan pocos ejemplos traseros.
'''

'''
Fundamentos de Agrupación (GroupBy) y Tablas Dinámicas (Pivot Tables):
El método groupby() agrupa datos según una o varias categorías para realizar cálculos sobre cada grupo (similar al GROUP BY de SQL).
'''

print("Valores únicos en drive-wheels:", df['drive-wheels'].unique())

# Agrupar por 'drive-wheels' y calcular el precio promedio:
df_grupo_uno = df[['drive-wheels', 'body-style', 'price']]
df_agrupado_traccion = df_grupo_uno.groupby(['drive-wheels'], as_index=False).agg({'price': 'mean'})
print("Precio promedio agrupado por tipo de tracción:\n", df_agrupado_traccion)

'''
Conclusión:
Los vehículos con tracción trasera ('rwd') son en promedio notablemente más caros, mientras que 4WD y delantera ('fwd') son más cercanos entre sí.
'''

# Agrupación múltiple por 'drive-wheels' y 'body-style':
df_agrupado_multiple = df_grupo_uno.groupby(['drive-wheels', 'body-style'], as_index=False).agg({'price': 'mean'})
print("Agrupación múltiple por tracción y estilo de carrocería:\n", df_agrupado_multiple)

# Convertir el DataFrame agrupado en una Tabla Dinámica (Pivot Table):
tabla_pivote = df_agrupado_multiple.pivot(index='drive-wheels', columns='body-style', values='price')
print("Tabla dinámica (Pivot Table):\n", tabla_pivote)

# Rellenar valores nulos de combinaciones inexistentes con 0:
tabla_pivote = tabla_pivote.fillna(0)
print("Tabla dinámica con nulos imputados en 0:\n", tabla_pivote)

'''
Pregunta 4:
Usa la función groupby para encontrar el precio promedio de cada coche según su 'body-style'.
'''
df_agrupado_estilo = df[['body-style', 'price']].groupby(['body-style'], as_index=False).mean()
print("Precio promedio según estilo de carrocería:\n", df_agrupado_estilo)

# Visualización con Mapa de Calor (Heatmap) de la relación Tracción vs Estilo de Carrocería respecto al Precio:
fig, ax = plt.subplots()
mapa_calor = ax.pcolor(tabla_pivote, cmap='RdBu')

etiquetas_columnas = tabla_pivote.columns
etiquetas_filas = tabla_pivote.index

# Centrar las marcas en las celdas
ax.set_xticks(np.arange(tabla_pivote.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(tabla_pivote.shape[0]) + 0.5, minor=False)

ax.set_xticklabels(etiquetas_columnas, minor=False)
ax.set_yticklabels(etiquetas_filas, minor=False)
plt.xticks(rotation=90)
plt.title("Mapa de Calor: Precio según Tracción y Estilo de Carrocería")
fig.colorbar(mapa_calor)
plt.show()

'''
Correlación y Causalidad:
- Correlación: mide el grado de interdependencia o relación entre variables.
- Causalidad: relación directa de causa y efecto.
Regla fundamental: Correlación NO implica causalidad.

Coeficiente de Correlación de Pearson (r):
- Mide la relación lineal entre dos variables continuas (-1 a +1).
- +1: Correlación lineal positiva perfecta.
-  0: Sin correlación lineal.
- -1: Correlación lineal negativa perfecta.

Valor p (p-value):
Mide la significancia estadística (probabilidad de que la correlación observada sea por azar):
- p-value < 0.001: Evidencia muy fuerte de que la correlación es significativa.
- p-value < 0.05:  Evidencia moderada de que es significativa.
- p-value < 0.1:   Evidencia débil.
- p-value >= 0.1:  No hay evidencia de correlación significativa.
'''

print("\n--- CÁLCULO DE COEFICIENTES DE PEARSON Y P-VALUES CON SCIPY.STATS ---\n")

# 1. Distancia entre ejes (wheel-base) vs Precio:
coef_pearson, valor_p = stats.pearsonr(df['wheel-base'], df['price'])
print(f"Wheel-base vs Precio: Coeficiente = {coef_pearson:.4f}, p-value = {valor_p:.4e}")
# Conclusión: Significativo (p < 0.001), relación moderada (~0.585).

# 2. Caballos de fuerza (horsepower) vs Precio:
coef_pearson, valor_p = stats.pearsonr(df['horsepower'], df['price'])
print(f"Horsepower vs Precio: Coeficiente = {coef_pearson:.4f}, p-value = {valor_p:.4e}")
# Conclusión: Significativo (p < 0.001), relación lineal bastante fuerte (~0.809).

# 3. Longitud (length) vs Precio:
coef_pearson, valor_p = stats.pearsonr(df['length'], df['price'])
print(f"Length vs Precio: Coeficiente = {coef_pearson:.4f}, p-value = {valor_p:.4e}")
# Conclusión: Significativo (p < 0.001), relación moderadamente fuerte (~0.691).

# 4. Ancho (width) vs Precio:
coef_pearson, valor_p = stats.pearsonr(df['width'], df['price'])
print(f"Width vs Precio: Coeficiente = {coef_pearson:.4f}, p-value = {valor_p:.4e}")
# Conclusión: Significativo (p < 0.001), relación bastante fuerte (~0.751).

# 5. Peso en vacío (curb-weight) vs Precio:
coef_pearson, valor_p = stats.pearsonr(df['curb-weight'], df['price'])
print(f"Curb-weight vs Precio: Coeficiente = {coef_pearson:.4f}, p-value = {valor_p:.4e}")
# Conclusión: Significativo (p < 0.001), relación bastante fuerte (~0.834).

# 6. Tamaño del motor (engine-size) vs Precio:
coef_pearson, valor_p = stats.pearsonr(df['engine-size'], df['price'])
print(f"Engine-size vs Precio: Coeficiente = {coef_pearson:.4f}, p-value = {valor_p:.4e}")
# Conclusión: Significativo (p < 0.001), relación lineal muy fuerte (~0.872).

# 7. Diámetro del cilindro (bore) vs Precio:
coef_pearson, valor_p = stats.pearsonr(df['bore'], df['price'])
print(f"Bore vs Precio: Coeficiente = {coef_pearson:.4f}, p-value = {valor_p:.4e}")
# Conclusión: Significativo (p < 0.001), relación lineal moderada (~0.521).

# 8. Rendimiento urbano (city-mpg) vs Precio:
coef_pearson, valor_p = stats.pearsonr(df['city-mpg'], df['price'])
print(f"City-mpg vs Precio: Coeficiente = {coef_pearson:.4f}, p-value = {valor_p:.4e}")
# Conclusión: Significativo (p < 0.001), relación negativa moderadamente fuerte (~ -0.687).

# 9. Rendimiento en autopista (highway-mpg) vs Precio:
coef_pearson, valor_p = stats.pearsonr(df['highway-mpg'], df['price'])
print(f"Highway-mpg vs Precio: Coeficiente = {coef_pearson:.4f}, p-value = {valor_p:.4e}")
# Conclusión: Significativo (p < 0.001), relación negativa moderadamente fuerte (~ -0.705).

'''
========================================================================================
CONCLUSIÓN FINAL DEL EDA: VARIABLES IMPORTANTES PARA PREDECIR EL PRECIO
========================================================================================
Tras analizar las correlaciones lineales, la significancia estadística (p-values < 0.001)
y las distribuciones categóricas, hemos identificado las variables más influyentes:

Variables Numéricas Continuas Clave:
1. Longitud (Length)
2. Ancho (Width)
3. Peso en vacío (Curb-weight)
4. Tamaño del motor (Engine-size) - La más fuerte (~0.87)
5. Caballos de fuerza (Horsepower) - Muy fuerte (~0.81)
6. Millas por galón en ciudad (City-mpg) - Fuerte negativa (~ -0.69)
7. Millas por galón en autopista (Highway-mpg) - Fuerte negativa (~ -0.71)
8. Distancia entre ejes (Wheel-base)
9. Diámetro del cilindro (Bore)

Variables Categóricas Clave:
- Tipo de tracción (Drive-wheels): marca diferencias claras de precio en los datos.

Al construir modelos predictivos de Machine Learning, alimentar el algoritmo únicamente con 
las variables que realmente impactan la variable objetivo (precio) mejorará notablemente la 
precisión y evitará el sobreajuste (ruido innecesario).
========================================================================================
'''
