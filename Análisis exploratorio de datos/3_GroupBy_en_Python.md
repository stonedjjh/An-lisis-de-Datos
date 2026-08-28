# 3. GroupBy y Tablas Dinámicas en Python

Una técnica poderosísima en el Análisis Exploratorio de Datos (EDA) es agrupar la información para compararla. Imagina que quieres saber si el tipo de tracción del auto y su estilo de carrocería afectan directamente al precio.

## Agrupación Básica: `groupby()`
En Pandas, el método `groupby()` se utiliza en variables categóricas (texto/categorías) para dividir los datos en subconjuntos. 

Puedes agrupar por una o múltiples variables al mismo tiempo, y luego aplicarle una operación matemática (como el promedio `mean()`) para ver el resultado de ese grupo específico.

**Ejemplo:** Queremos saber el precio promedio dependiendo del tipo de tracción (`drive-wheels`) y la carrocería (`body-style`).
```python
# 1. Seleccionamos solo las 3 columnas que nos interesan
df_test = df[['drive-wheels', 'body-style', 'price']]

# 2. Agrupamos por tracción y carrocería, y calculamos el promedio (mean) del precio
df_grp = df_test.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
```
*El resultado de este código nos dirá, por ejemplo, que los descapotables con tracción trasera son los más caros, mientras que los compactos 4x4 son los más baratos.*

---

## Tablas Dinámicas (Pivot Tables)
El resultado del código anterior es una lista larga que no es muy fácil de leer ni de graficar. Para solucionarlo, podemos transformarla en una **Tabla Dinámica (Pivot Table)**, tal como lo harías en Excel.

Una tabla dinámica toma una variable y la pone en las filas, y toma otra variable y la pone en las columnas. Así, los precios quedan en una cuadrícula (matriz) perfecta.

Usamos el método `pivot()`:
```python
# Convertimos el grupo en una tabla dinámica
# Filas (index): tracción | Columnas (columns): carrocería
df_pivot = df_grp.pivot(index='drive-wheels', columns='body-style')
```

---

## Visualización Avanzada: Mapas de Calor (Heatmaps)
La mejor forma visual de interpretar una Tabla Dinámica es usando un **Mapa de Calor**. 

Un Heatmap toma esa cuadrícula rectangular de precios y le asigna una **intensidad de color** basada en el valor. Es ideal para comparar una variable objetivo frente a múltiples variables categóricas.

- Colores cálidos/oscuros pueden representar precios altos.
- Colores fríos/claros pueden representar precios bajos.

**Ejemplo conceptual (Matplotlib):**
```python
import matplotlib.pyplot as plt

# Usamos pcolor para generar el mapa de calor basado en nuestra tabla dinámica
plt.pcolor(df_pivot, cmap='RdBu') # RdBu = Esquema Rojo-Azul
plt.colorbar() # Muestra la barra guía de colores al lado
plt.show()
```
Al visualizarlo de esta manera, en lugar de leer números, simplemente buscas los bloques de color rojo fuerte para saber inmediatamente qué combinaciones de autos son las más costosas del mercado.
