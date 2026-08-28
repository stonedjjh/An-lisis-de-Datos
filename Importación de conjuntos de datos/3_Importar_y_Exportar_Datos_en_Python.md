# 3. Importar y Exportar Datos en Python

El primer paso fundamental en el análisis de datos es la **adquisición de datos**, que consiste en leer e importar la información a nuestro entorno (como un Jupyter Notebook).

Para leer datos usando Pandas, hay dos factores críticos a considerar:
1.  **Formato:** La forma en que están codificados los datos (CSV, JSON, XLSX, HDF, etc.). Generalmente se sabe viendo la extensión del archivo.
2.  **Ruta (File Path):** Dónde están almacenados (localmente en la PC o en internet mediante una URL).

## Importar Datos (Leer)
En Pandas, la función principal para importar archivos CSV es `read_csv()`.

```python
import pandas as pd

# 1. Definir la ruta (local o URL)
ruta = "ruta/al/archivo.csv"

# 2. Leer el archivo
df = pd.read_csv(ruta)
```

**Manejo de Cabeceras (Headers):**
Por defecto, `read_csv` asume que la primera fila tiene los nombres de las columnas. Si tu archivo *no* tiene cabeceras (como nuestro ejemplo de autos), debes indicarlo explícitamente para no perder esa primera fila de datos:
```python
df = pd.read_csv(ruta, header=None)
```

**Asignar Nombres a las Columnas:**
Si importaste sin cabeceras, Pandas pondrá números enteros (0, 1, 2...) como nombres de columna. Puedes cambiarlos pasando una lista con los nombres correctos:
```python
headers = ["symboling", "normalized-losses", "make", ...] # Lista completa
df.columns = headers
```

## Exploración Rápida
Imprimir todo el dataset puede saturar la memoria. Para revisar rápidamente que la importación fue exitosa usamos:
-   `df.head(n)`: Muestra las primeras *n* filas del dataframe (por defecto 5).
-   `df.tail(n)`: Muestra las últimas *n* filas del dataframe.

## Exportar Datos (Guardar)
Después de procesar, limpiar o analizar los datos, es probable que quieras guardar los resultados en un archivo nuevo. En Pandas, puedes exportar tu DataFrame de vuelta a un archivo CSV usando el método `to_csv()`.

```python
# Guardar el DataFrame en tu computadora
df.to_csv("autos_limpios.csv")
```
*Nota: Pandas soporta importar y exportar muchísimos formatos diferentes usando sintaxis similares, como `read_excel()` o `to_json()`.*
