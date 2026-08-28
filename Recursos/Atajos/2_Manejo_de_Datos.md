# Hoja de Trucos del Módulo 2: Manejo de Datos

| Paquete/Método | Descripción | Código de Ejemplo |
| :--- | :--- | :--- |
| **Sustituir datos ausentes por frecuencia** | Sustituye los valores que faltan por la entrada más común (la moda) de la columna. | ```python<br>MostFrequentEntry = df['attribute_name'].value_counts().idxmax()<br>df['attribute_name'].replace(np.nan, MostFrequentEntry, inplace=True)<br>``` |
| **Sustituir datos ausentes por la media** | Sustituye los valores que faltan por el promedio (media) de todas las entradas numéricas de la columna. | ```python<br>AverageValue = df['attribute_name'].astype('float').mean(axis=0)<br>df['attribute_name'].replace(np.nan, AverageValue, inplace=True)<br>``` |
| **Corregir tipos de datos** | Corrige o convierte los tipos de datos de las columnas del dataframe. | ```python<br>df[['attr1', 'attr2']] = df[['attr1', 'attr2']].astype('data_type')<br># data_type puede ser 'int', 'float', etc.<br>``` |
| **Normalización de datos** | Normaliza los datos de una columna dividiéndolos por el máximo, para que oscilen entre 0 y 1. | ```python<br>df['attribute_name'] = df['attribute_name'] / df['attribute_name'].max()<br>``` |
| **Binning** | Crea intervalos o categorías para un mejor análisis y visualización de datos continuos. | ```python<br>bins = np.linspace(min(df['attribute_name']), max(df['attribute_name']), n)<br># n es el número de divisores<br>GroupNames = ['Group1', 'Group2', 'Group3']<br>df['binned_attr'] = pd.cut(df['attribute_name'], bins, labels=GroupNames, include_lowest=True)<br>``` |
| **Cambiar nombre de columna** | Cambia o renombra la etiqueta de una o varias columnas del dataframe. | ```python<br>df.rename(columns={'old_name': 'new_name'}, inplace=True)<br>``` |
| **Variables indicadoras** | Crea variables indicadoras (Dummy Variables binarias) para transformar datos categóricos en numéricos. | ```python<br>dummy_variable = pd.get_dummies(df['attribute_name'])<br>df = pd.concat([df, dummy_variable], axis=1)<br>``` |
