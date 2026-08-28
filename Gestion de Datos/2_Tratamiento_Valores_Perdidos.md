# Tratamiento de Valores Perdidos en Python

En el análisis de datos, es muy común enfrentarse al problema de los **valores perdidos** (missing values). Esto ocurre cuando no se almacena ningún dato para una característica u observación en particular.

Generalmente, los valores perdidos aparecen en los datasets como signos de interrogación (?), N/A, ceros, o simplemente celdas en blanco. En Python (a través de Pandas), suelen representarse por defecto como NaN (Not a Number).

## Estrategias para manejar los Valores Perdidos

Cada dataset y situación es diferente, por lo que el enfoque debe evaluarse caso por caso. Sin embargo, estas son las opciones más comunes:

1. **Recuperar el valor real:** Contactar a la persona o sistema que recopiló los datos para obtener el valor correcto y original.
2. **Eliminar los datos (Drop):** 
   - Puedes eliminar toda la variable (la columna entera).
   - O puedes eliminar solo la entrada individual (la fila) que contiene el valor perdido. 
   - *Nota:* Si hay pocas observaciones con datos faltantes, eliminar esas filas suele ser la mejor opción. Si vas a eliminar datos, el objetivo siempre es buscar el menor impacto posible.
3. **Reemplazar los datos (Replace):**
   - Generalmente es mejor que eliminarlos porque no se desperdicia información, aunque es menos preciso ya que se basa en una suposición o estimación.
   - **Para variables numéricas:** Una técnica estándar es reemplazar el valor perdido por el **promedio (media)** de toda esa columna.
   - **Para variables categóricas:** Dado que no se puede calcular un promedio de palabras (ej. tipo de combustible), se suele reemplazar por la **moda** (el valor más frecuente o común).
   - **Estimación experta:** A veces, quien recopiló los datos tiene información adicional para hacer una estimación mucho más precisa.
4. **Dejar los datos como perdidos:** En ciertos contextos estadísticos, el simple hecho de que falte un dato es información útil y se debe conservar tal cual.

---

## Implementación en Python (con Pandas)

### 1. Eliminar Valores Perdidos (dropna)
La biblioteca Pandas tiene el método incorporado dropna() para descartar filas o columnas que contienen valores NaN.

- `axis=0`: Elimina las **filas** que contienen el valor perdido.
- `axis=1`: Elimina las **columnas** que contienen el valor perdido.

```python
# Elimina las filas con valores perdidos en todo el dataframe
df.dropna(aaxis=0, inplace=True)
```
*Importante:* El parámetro inplace=True escribe el resultado directamente sobre el propio dataframe modificándolo permanentemente. Es equivalente a hacer df = df.dropna(aaxis=0).

### 2. Reemplazar Valores Perdidos (Replace)
Pandas cuenta con el método 
replace(), que permite buscar un valor y sustituirlo por otro.
df.replace(missing_value, new_value)

```python
# Ejemplo: Calcular el promedio y reemplazar los NaN de una columna específica
mean_value = df['normalized-losses'].mean()

# replace(valor_a_buscar, valor_de_reemplazo)
df['normalized-losses'].replace(np.nan, mean_value, inplace=True)
```
