import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# 1. Cargar el conjunto de datos
nombre_archivo = "laptop_pricing_dataset_mod2.csv"
df = pd.read_csv(nombre_archivo, header=0)

# Imprimir las primeras 5 filas para confirmar la carga
print("Primeras 5 filas del dataset de portátiles:\n", df.head(5))

'''
========================================================================================
Tarea 1: Visualizar Patrones de Características Individuales
========================================================================================

A. Características Numéricas Continuas:
Generar gráficos de regresión (regplot) para los parámetros "CPU_frequency", "Screen_Size_inch" 
y "Weight_pounds" frente al precio ("Price"). 
Además, calcular e imprimir la correlación de cada una de estas variables con el precio.
'''

# 1. Gráfico de Frecuencia de la CPU (CPU_frequency) vs Precio
sns.regplot(x="CPU_frequency", y="Price", data=df)
plt.ylim(0,)
plt.title("Frecuencia de CPU vs Precio")
plt.xlabel("Frecuencia de CPU (GHz)")
plt.ylabel("Precio ($)")
plt.show()

# 2. Gráfico de Tamaño de Pantalla (Screen_Size_inch) vs Precio
sns.regplot(x="Screen_Size_inch", y="Price", data=df)
plt.ylim(0,)
plt.title("Tamaño de Pantalla vs Precio")
plt.xlabel("Tamaño de Pantalla (Pulgadas)")
plt.ylabel("Precio ($)")
plt.show()

# 3. Gráfico de Peso en Libras (Weight_pounds) vs Precio
sns.regplot(x="Weight_pounds", y="Price", data=df)
plt.ylim(0,)
plt.title("Peso vs Precio")
plt.xlabel("Peso (Libras)")
plt.ylabel("Precio ($)")
plt.show()

# Valores de correlación de los tres atributos continuos con el Precio
print("\n--- CORRELACIÓN DE ATRIBUTOS CONTINUOS CON EL PRECIO ---")
print("Correlación de CPU_frequency con Price:", df["CPU_frequency"].corr(df["Price"]))
print("Correlación de Screen_Size_inch con Price:", df["Screen_Size_inch"].corr(df["Price"]))
print("Correlación de Weight_pounds con Price:", df["Weight_pounds"].corr(df["Price"]))

'''
Interpretación:
- "CPU_frequency" tiene una correlación positiva moderada (~0.37 o 37%) con el precio: a mayor frecuencia, tiende a subir el precio.
- Los otros dos parámetros ("Screen_Size_inch" con -0.11 y "Weight_pounds" con -0.05) tienen correlaciones muy débiles/casi nulas con el precio.

----------------------------------------------------------------------------------------
B. Características Categóricas:
Generar diagramas de caja y bigotes (Boxplots) para las variables categóricas o discretas:
"Category", "GPU", "OS", "CPU_core", "RAM_GB", "Storage_GB_SSD"
'''

# Boxplot por Categoría (Category)
sns.boxplot(x="Category", y="Price", data=df)
plt.title("Categoría de Portátil vs Precio")
plt.xlabel("Categoría")
plt.ylabel("Precio ($)")
plt.show()

# Boxplot por Tarjeta Gráfica (GPU)
sns.boxplot(x="GPU", y="Price", data=df)
plt.title("Nivel de GPU vs Precio")
plt.xlabel("GPU")
plt.ylabel("Precio ($)")
plt.show()

# Boxplot por Sistema Operativo (OS)
sns.boxplot(x="OS", y="Price", data=df)
plt.title("Sistema Operativo (OS) vs Precio")
plt.xlabel("OS")
plt.ylabel("Precio ($)")
plt.show()

# Boxplot por Núcleos de CPU (CPU_core)
sns.boxplot(x="CPU_core", y="Price", data=df)
plt.title("Núcleos de CPU vs Precio")
plt.xlabel("Núcleos de CPU")
plt.ylabel("Precio ($)")
plt.show()

# Boxplot por Memoria RAM (RAM_GB)
sns.boxplot(x="RAM_GB", y="Price", data=df)
plt.title("Memoria RAM (GB) vs Precio")
plt.xlabel("RAM (GB)")
plt.ylabel("Precio ($)")
plt.show()

# Boxplot por Almacenamiento SSD (Storage_GB_SSD)
sns.boxplot(x="Storage_GB_SSD", y="Price", data=df)
plt.title("Almacenamiento SSD (GB) vs Precio")
plt.xlabel("Almacenamiento SSD (GB)")
plt.ylabel("Precio ($)")
plt.show()


'''
========================================================================================
Tarea 2: Análisis Estadístico Descriptivo
========================================================================================
Generar la descripción estadística de todas las características utilizadas en el dataset,
incluyendo también los tipos de datos de texto/objeto.
'''

print("\n--- DESCRIPCIÓN ESTADÍSTICA DE VARIABLES NUMÉRICAS ---")
print(df.describe())

print("\n--- DESCRIPCIÓN ESTADÍSTICA DE VARIABLES CATEGÓRICAS / OBJETO ---")
print(df.describe(include=['object']))


'''
========================================================================================
Tarea 3: Agrupación (GroupBy) y Tablas Dinámicas (Pivot Tables)
========================================================================================
Agrupar los parámetros "GPU", "CPU_core" y "Price" para construir una tabla dinámica 
y visualizar esta relación usando un gráfico de mapa de color (pcolor / heatmap).
'''

# 1. Crear el subconjunto y agrupar calculando la media del precio
df_grupo = df[['GPU', 'CPU_core', 'Price']]
df_agrupado = df_grupo.groupby(['GPU', 'CPU_core'], as_index=False).mean()
print("\n--- DATAFRAME AGRUPADO POR GPU Y CPU_CORE (PRECIO PROMEDIO) ---")
print(df_agrupado)

# 2. Crear la Tabla Dinámica (Pivot Table): Filas = GPU, Columnas = CPU_core
tabla_pivote = df_agrupado.pivot(index='GPU', columns='CPU_core', values='Price')
print("\n--- TABLA DINÁMICA (PIVOT TABLE) ---")
print(tabla_pivote)

# 3. Graficar con pcolor / mapa de calor
fig, ax = plt.subplots()
mapa = ax.pcolor(tabla_pivote, cmap='RdBu')

# Nombres de etiquetas
etiquetas_columnas = tabla_pivote.columns
etiquetas_filas = tabla_pivote.index

# Centrar las marcas en el medio de cada celda
ax.set_xticks(np.arange(tabla_pivote.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(tabla_pivote.shape[0]) + 0.5, minor=False)

# Insertar las etiquetas correspondientes
ax.set_xticklabels(etiquetas_columnas, minor=False)
ax.set_yticklabels(etiquetas_filas, minor=False)

plt.title("Mapa de Calor: Precio Promedio según GPU y CPU_core")
plt.xlabel("Núcleos de CPU (CPU_core)")
plt.ylabel("Nivel de GPU")
fig.colorbar(mapa)
plt.show()


'''
========================================================================================
Tarea 4: Correlación de Pearson y Valores p (p-values)
========================================================================================
Usar la función scipy.stats.pearsonr() para evaluar el Coeficiente de Pearson y el p-value 
de cada parámetro evaluado frente a 'Price'.
Esto permite determinar cuáles variables tienen un efecto real y estadísticamente significativo 
sobre el precio de los portátiles.
'''

parametros = [
    'RAM_GB', 'CPU_frequency', 'Storage_GB_SSD', 'Screen_Size_inch',
    'Weight_pounds', 'CPU_core', 'OS', 'GPU', 'Category'
]

print("\n--- EVALUACIÓN DE COEFICIENTES DE PEARSON Y P-VALUES ---")
for param in parametros:
    coef_pearson, valor_p = stats.pearsonr(df[param], df['Price'])
    print(f"\nParámetro: {param}")
    print(f"  -> Coeficiente de Pearson (r): {coef_pearson:.4f}")
    print(f"  -> Valor p (p-value): {valor_p:.4e}")
    
    # Interpretación automática rápida
    if valor_p < 0.001:
        significancia = "Muy fuerte evidencia de significancia (p < 0.001)"
    elif valor_p < 0.05:
        significancia = "Significativo (p < 0.05)"
    else:
        significancia = "NO estadísticamente significativo (p >= 0.05, posible azar)"
    print(f"  -> Conclusión: {significancia}")

'''
========================================================================================
RESUMEN Y CONCLUSIÓN FINAL:
========================================================================================
1. Variables con mayor impacto positivo en el precio:
   - RAM_GB (r ≈ 0.55, p ≈ 3.68e-20): La memoria RAM es el predictor individual más fuerte.
   - CPU_core (r ≈ 0.46, p ≈ 7.91e-14): Más núcleos se traducen directamente en mayor precio.
   - CPU_frequency (r ≈ 0.37, p ≈ 5.50e-09): Frecuencia de reloj influye notablemente.
   - GPU (r ≈ 0.29, p ≈ 6.17e-06) y Category (r ≈ 0.29, p ≈ 7.23e-06): Correlaciones moderadas.
   - Storage_GB_SSD (r ≈ 0.24, p ≈ 0.0001): Correlación moderada/positiva.

2. Variables sin impacto o débiles:
   - Weight_pounds (r ≈ -0.05, p ≈ 0.44): p-value > 0.05, no hay relación estadística con el precio.
   - Screen_Size_inch (r ≈ -0.11, p ≈ 0.088): p-value > 0.05, relación insignificante o puro azar.
========================================================================================
'''
