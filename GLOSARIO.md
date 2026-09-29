# 📖 Glosario de Análisis de Datos (Enfoque Developer)

Este glosario traduce los términos clave de la Ciencia y Análisis de Datos a conceptos y analogías familiares para desarrolladores de software.

---

## 📑 Índice Rápido
1. [Limpieza y Preparación (Data Wrangling)](#1-limpieza-y-preparación-data-wrangling)
2. [Estadística Descriptiva y Distribuciones](#2-estadística-descriptiva-y-distribuciones)
3. [Análisis Exploratorio (EDA) y Relaciones](#3-análisis-exploratorio-eda-y-relaciones)
4. [Visualización de Datos](#4-visualización-de-datos)

---

## 1. Limpieza y Preparación (Data Wrangling)

### **Data Wrangling / Data Cleaning**
- **Definición:** Proceso de transformar, limpiar y estructurar datos en bruto a un formato apto para el análisis o modelado.
- **Mentalidad Dev:** Es el pipeline de sanitización, validación y formateo de datos de entrada (`input parsing / sanitization`).

### **Valores Faltantes (`NaN`, `None`, `null`)**
- **Definición:** Celdas sin valor o corruptas.
- **Técnicas habituales:**
  - **Eliminación (`dropna`):** Borrar la fila/columna (como descartar un payload corrupto).
  - **Imputación (`fillna`):** Sustituir el nulo por un valor calculado (media, mediana o valor por defecto).

### **Imputación (Imputation)**
- **Definición:** Rellenar valores vacíos con una aproximación razonable basada en los datos existentes.
- **Mentalidad Dev:** Asignar un *fallback* o valor por defecto calculado (`default value fallback`).

### **Normalización / Escalado (Scaling)**
- **Definición:** Ajustar diferentes variables numéricas con magnitudes muy distintas a una escala uniforme.
  - **Min-Max Scaling:** Escala todo al rango $[0, 1]$.
  - **Z-score (Estandarización):** Centra la media en 0 con desviación estándar de 1.
- **Mentalidad Dev:** Como normalizar vectores en gráficos 3D o transformar diferentes unidades (bytes, KB, MB) a un float entre 0 y 1 para una barra de progreso.

### **Binning (Discretización / Agrupación en Cubetas)**
- **Definición:** Convertir una variable numérica continua en rangos o categorías discretas (ej. edades de 18 a 80 agrupadas en `Joven`, `Adulto`, `Senior`).
- **Mentalidad Dev:** Una función `switch / case` o condicionales por rangos (`if (edad < 25) return "Joven"`).

### **One-Hot Encoding (Variables Dummy)**
- **Definición:** Convertir categorías de texto no jerárquicas en múltiples columnas booleanas ($0$ o $1$).
- **Mentalidad Dev:** Convertir un `enum` o string en un mapa de flags binarios (`bitmask` o flags booleanos).

---

## 2. Estadística Descriptiva y Distribuciones

### **Media (Mean / Promedio)**
- **Definición:** La suma de todos los valores dividida por el total de registros.
- **Cuidado:** Muy sensible a valores atípicos (*outliers*).

### **Mediana (Median)**
- **Definición:** El valor que queda exactamente en el centro (percentil 50) al ordenar los datos.
- **Mentalidad Dev:** El elemento en el índice `arr[len(arr) // 2]` tras un `sort()`. Resistente a datos basura o valores extremos.

### **Moda (Mode)**
- **Definición:** El valor que más veces se repite en el conjunto.
- **Mentalidad Dev:** La clave con mayor conteo en un `Map<Valor, Frecuencia>`.

### **Outlier (Valor Atípico)**
- **Definición:** Un dato numérico que difiere drásticamente del resto del conjunto (muy alto o muy bajo).
- **Mentalidad Dev:** Una anomalía o valor fuera de contrato (`anomaly / spike`), como una latencia de 10,000 ms cuando el p95 es 50 ms.

### **Varianza y Desviación Estándar**
- **Definición:** Medida de qué tan dispersos están los datos respecto a su promedio.
  - Si es baja, casi todos los valores están apiñados cerca de la media.
  - Si es alta, hay mucha dispersión.

---

## 3. Análisis Exploratorio (EDA) y Relaciones

### **EDA (Exploratory Data Analysis)**
- **Definición:** La fase de análisis inicial para entender la estructura, anomalías y relaciones en los datos antes de crear modelos.
- **Mentalidad Dev:** La fase de introspección / debugging / profilado inicial de un sistema o base de datos.

### **GroupBy (Agrupación)**
- **Definición:** Dividir los datos en grupos según una o más categorías para aplicar funciones agregadas (`mean`, `sum`, `count`).
- **Mentalidad Dev:** Idéntico al `GROUP BY` de SQL o un `reduce()` por clave en JavaScript/Python.

### **Coeficiente de Correlación de Pearson ($r$)**
- **Definición:** Número entre **-1.0 y +1.0** que cuantifica la fuerza y la dirección de una relación lineal entre dos variables numéricas continuas.
  - **Signo ($+$ o $-$):** **Dirección**.
    - **Positivo ($+$):** Ambas variables crecen juntas (ej. `horas_estudio` $\uparrow$ $\rightarrow$ `nota` $\uparrow$).
    - **Negativo ($-$)**: Se mueven en sentido inverso (ej. `antigüedad_auto` $\uparrow$ $\rightarrow$ `precio` $\downarrow$).
  - **Magnitud (valor absoluto):** **Fuerza**.
    - $0.00$ a $0.20$: Nula o muy débil (puro ruido).
    - $0.20$ a $0.50$: Débil a moderada.
    - $0.50$ a $0.80$: Moderada a fuerte.
    - $0.80$ a $1.00$: Muy fuerte / casi lineal perfecta.
- **Mentalidad Dev:** Es un score normalizado de acoplamiento lineal entre dos variables (como calcular qué tan sincronizadas están dos métricas en un dashboard).
- **Cuidado:** No detecta relaciones curvas o no lineales, y *correlación no implica causalidad*.

### **p-value (Valor p / Nivel de Significancia Estadística)**
- **Definición:** La probabilidad de que el resultado observado (como una correlación o una diferencia de promedios) sea producto de la **pura casualidad o del azar**.
  - Si el **$p\text{-value}$ es muy pequeño ($p < 0.05$ o $5\%$)**: Significa que es sumamente improbable que sea casualidad. Concluimos que el resultado es **estadísticamente significativo** (podemos confiar en él).
  - Si el **$p\text{-value}$ es grande ($p \ge 0.05$)**: No podemos descartar que haya sido pura coincidencia o ruido en la muestra.
- **Mentalidad Dev:** Piensa en una **tasa de falsos positivos aceptable** o un test flaky. 
  - Un test de hipótesis asume por defecto la *Hipótesis Nula* ($H_0$: "aquí no hay nada real, es puro azar").
  - El $p\text{-value}$ es la probabilidad de que tu alerta sea un falso positivo. Si esa probabilidad es menor al $5\%$ ($p < 0.05$), consideras que el bug/patrón es real y rechazas la hipótesis de azar.
- **En conjunto con la Correlación:**
  - $r = 0.85$ con $p < 0.001$: Correlación fuertísima y **confiable al 99.9%**.
  - $r = 0.85$ con $p = 0.40$: Parece fuerte, pero la muestra es tan pequeña o ruidosa que hay un 40% de riesgo de que sea pura coincidencia. **No te fíes**.

### **ANOVA (Analysis of Variance)**
- **Definición:** Prueba estadística para determinar si existen diferencias significativas entre las medias de dos o más grupos distintos (ej. precio promedio según tracción: 4WD vs FWD vs RWD).
- **F-test (F-score):** Mide la variación entre los grupos respecto a la variación interna de cada grupo. Un $F$ alto significa que los grupos son realmente distintos entre sí.
- **p-value en ANOVA:** Confirma si esa diferencia observada entre grupos es real ($p < 0.05$) o solo ruido.

---

## 4. Visualización de Datos

### **Histograma**
- **Uso:** Ver la forma de distribución de **1 sola variable numérica** (frecuencia de ocurrencia por rangos).

### **Scatter Plot (Diagrama de Dispersión)**
- **Uso:** Graficar pares de coordenadas $(x, y)$ para identificar visualmente la correlación o patrones entre **2 variables numéricas**.

### **Boxplot (Diagrama de Caja y Bigotes)**
- **Uso:** Comparar distribuciones y detectar outliers rápidamente. Muestra:
  - Mediana (línea central).
  - Cuartiles Q1 y Q3 (caja = 50% central de los datos).
  - Bigotes (rango de valores esperados).
  - Puntos exteriores (outliers).
