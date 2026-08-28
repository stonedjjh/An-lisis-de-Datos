# Análisis de datos con Python
## Hoja de trucos: Importación de conjuntos de datos

| Paquete/Método | Descripción | Código Ejemplo |
| :--- | :--- | :--- |
| **Leer conjunto de datos CSV** | Leer el archivo CSV que contiene un conjunto de datos a un marco de datos pandas | ```python\ndf = pd.read_csv(<CSV_path>, header = None)  # load without header\ndf = pd.read_csv(<CSV_path>, header = 0)  # load using first row as header\n``` |
| **Imprimir las primeras entradas** | Imprime las primeras entradas (por defecto 5) del marco de datos de pandas | ```python\ndf.head(n) #n=number of entries; default 5\n``` |
| **Imprimir las últimas entradas** | Imprime las últimas entradas (por defecto 5) del marco de datos de pandas | ```python\ndf.tail(n) #n=number of entries; default 5\n``` |
| **Asignar nombres de cabecera** | Asignar nombres de cabecera apropiados al marco de datos | ```python\ndf.columns = headers\n``` |
| **Sustituir "?" por NaN** | Reemplazar las entradas "?" por una entrada NaN de la librería Numpy | ```python\ndf = df.replace("?", np.nan)\n``` |
| **Recuperar tipos de datos** | Recuperar los tipos de datos de las columnas del marco de datos | ```python\ndf.dtypes\n``` |
| **Recuperar la descripción estadística** | Recupera la descripción estadística del conjunto de datos. El uso por defecto es sólo para tipos de datos numéricos. Utilice include="all" para crear el resumen de todas las variables | ```python\ndf.describe() # default \ndf.describe(include="all")\n``` |
| **Recuperar resumen del conjunto de datos** | Recupera el resumen del conjunto de datos que se está utilizando, desde el marco de datos | ```python\ndf.info()\n``` |
| **Guardar marco de datos en CSV** | Guardar el marco de datos procesado en un archivo CSV con una ruta especificada | ```python\ndf.to_csv(<output CSV path>)\n``` |
