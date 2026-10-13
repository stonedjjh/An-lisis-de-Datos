# Hoja de Trucos del Módulo 3: Análisis Exploratorio de Datos (EDA)

| Paquete / Método | Descripción | Código de Ejemplo |
| :--- | :--- | :--- |
| **Correlación completa del DataFrame** | Matriz de correlación creada utilizando todos los atributos numéricos del conjunto de datos. | ```python<br>df.corr()<br>``` |
| **Correlación de atributos específicos** | Matriz de correlación calculada únicamente entre columnas numéricas seleccionadas. | ```python<br>df[['attribute1', 'attribute2', ...]].corr()<br>``` |
| **Gráfico de dispersión (Scatter Plot)** | Crea un diagrama de dispersión enfrentando la variable independiente en el eje X y la dependiente en el eje Y. | ```python<br>import matplotlib.pyplot as plt<br><br>plt.scatter(df['attribute_1'], df['attribute_2'])<br>plt.show()<br>``` |
| **Gráfico de regresión (Regplot)** | Genera un gráfico de dispersión junto con la recta de regresión lineal ajustada para modelar la tendencia. | ```python<br>import seaborn as sns<br><br>sns.regplot(x='attribute_1', y='attribute_2', data=df)<br>``` |
| **Gráfico de cajas y bigotes (Boxplot)** | Muestra la distribución, mediana, cuartiles y outliers de los datos agrupados por categorías. | ```python<br>import seaborn as sns<br><br>sns.boxplot(x='attribute_1', y='attribute_2', data=df)<br>``` |
| **Selección de subconjunto de atributos** | Crea un nuevo DataFrame seleccionando únicamente los atributos requeridos para el análisis agrupado. | ```python<br>df_group = df[['attribute_1', 'attribute_2', ...]]<br>``` |
| **Sentencias GroupBy** | **a)** Agrupar por un atributo categórico y calcular la media de las variables numéricas.<br>**b)** Agrupar por múltiples atributos categóricos calculando la media. | ```python<br># a) Un atributo<br>df_group = df.groupby(['attribute_1'], as_index=False).mean()<br><br># b) Múltiples atributos<br>df_group = df.groupby(['attribute_1', 'attribute_2'], as_index=False).mean()<br>``` |
| **Tablas Dinámicas (Pivot Tables)** | Reorganiza el DataFrame agrupado en una matriz bidimensional (filas y columnas) para facilitar su lectura. | ```python<br>grouped_pivot = df_group.pivot(index='attribute_1', columns='attribute_2', values='target_value')<br>``` |
| **Gráfico de pseudocolor (pcolor / Heatmap)** | Representa visualmente la tabla dinámica como un mapa de calor según la intensidad de los valores. | ```python<br>import matplotlib.pyplot as plt<br><br>plt.pcolor(grouped_pivot, cmap='RdBu')<br>plt.colorbar()<br>plt.show()<br>``` |
| **Coeficiente de Pearson y Valor p (p-value)** | Calcula el coeficiente de correlación de Pearson ($r$) y el nivel de significancia estadística ($p\text{-value}$). | ```python<br>from scipy import stats<br><br>pearson_coef, p_value = stats.pearsonr(df['attribute_1'], df['attribute_2'])<br>``` |
