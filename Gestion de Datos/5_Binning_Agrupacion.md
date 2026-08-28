# Binning (Agrupación de Datos)

El **Binning** (o agrupación) es un método de preprocesamiento de datos que consiste en agrupar valores numéricos continuos en "contenedores" (bins) o categorías discretas. 

Por ejemplo, si tienes una variable numérica de "edad", en lugar de tener números exactos puedes agruparla en rangos como: `0-5`, `6-10`, `11-15`, etc.

## ¿Para qué sirve el Binning?
1. **Mejorar modelos predictivos:** En ciertas ocasiones, agrupar los datos puede reducir el ruido (valores atípicos pequeños) y mejorar la precisión matemática de los modelos de predicción.
2. **Entender la distribución:** Agrupar una amplia gama de valores numéricos en unos pocos grupos facilita enormemente la comprensión visual e intuitiva de cómo se distribuyen los datos.

## Ejemplo Práctico: Rango de Precios
Imagina que en un dataset la característica "precio" (price) varía de $5,188 a $45,400, conteniendo más de 200 valores únicos diferentes. Analizar eso número por número es difícil, así que usamos Binning para categorizarlos en 3 grupos (bins):
- Precio Bajo (*Low*)
- Precio Medio (*Medium*)
- Precio Alto (*High*)

---

## Implementación en Python (con Pandas y NumPy)

Para dividir los datos en 3 grupos de exactamente el mismo tamaño (ancho del rango), matemáticamente necesitamos **4 puntos divisores** equidistantes.

### 1. Crear los divisores (`linspace`)
Usamos la función `linspace` de la librería NumPy para calcular y generar automáticamente estos 4 divisores:

```python
import numpy as np
import pandas as pd

# linspace(valor_mínimo, valor_máximo, cantidad_de_divisores)
bins = np.linspace(df["price"].min(), df["price"].max(), 4)
```

### 2. Definir los nombres de los grupos
Creamos una lista de Python normal con las etiquetas que le daremos a cada segmento:

```python
nombres_grupos = ['Low', 'Medium', 'High']
```

### 3. Agrupar y segmentar los datos (`pd.cut`)
Finalmente, usamos la función `cut` de Pandas. Esta función toma los datos originales de la columna, los divide usando los `bins` (divisores) y les asigna las etiquetas (`labels`).

```python
# Crea una nueva columna categórica ('price-binned') basada en el valor numérico
df['price-binned'] = pd.cut(df['price'], bins, labels=nombres_grupos, include_lowest=True)
```

### 4. Visualización
Una vez que los datos han sido agrupados, la práctica estándar es crear un **histograma** para visualizar la nueva distribución. Por ejemplo, al graficar la nueva columna `price-binned`, es posible notar a simple vista si la inmensa mayoría de los autos pertenecen a la categoría "Low", algo que con 200 números únicos no era tan evidente.
