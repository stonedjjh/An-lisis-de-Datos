import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------------------
# Carga inicial del conjunto de datos
# -------------------------------------------------------------------------
file_name = "../../Análisis exploratorio de datos/Precios de coches usados/automobileEDA.csv"
df = pd.read_csv(file_name)

print("=" * 70)
print("TUTORIAL INTERACTIVO: DESARROLLO DE MODELOS CON PYTHON")
print("=" * 70)
print("\nMostramos el dataframe de autos:\n")
print(df.head())
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

# -------------------------------------------------------------------------
# SECCIÓN 1: Regresión Lineal y Regresión Lineal Múltiple
# -------------------------------------------------------------------------
print("\n" + "=" * 70)
print("1. Regresión Lineal y Regresión Lineal Múltiple")
print("=" * 70)
print('''
Regresión Lineal

Un ejemplo de Modelo de Datos que utilizaremos es:

Regresión Lineal Simple (SLR)

La regresión lineal simple es un método que nos ayuda a comprender la relación
entre dos variables:
  * La variable predictora / independiente (X)
  * La variable de respuesta / dependiente (que deseamos predecir) (Y)

El resultado de la regresión lineal es una función lineal que predice la
variable de respuesta (dependiente) en función de la variable predictora (independiente).

Y: Variable de respuesta
X: Variable predictora

Función Lineal:
    Yhat = a + bX

* a se refiere al intercepto de la línea de regresión; en otras palabras, el
  valor de Y cuando X es 0.
* b se refiere a la pendiente de la línea de regresión; en otras palabras, el
  valor en el que cambia Y cuando X aumenta en 1 unidad.

Carguemos los módulos para la regresión lineal:

Código a ejecutar:
    from sklearn.linear_model import LinearRegression
''')
input("Presione Enter para continuar...")

from sklearn.linear_model import LinearRegression

print('''
Crear el objeto de regresión lineal:

Código a ejecutar:
    lm = LinearRegression()
    print(lm)
''')
lm = LinearRegression()
print("Salida:")
print(lm)
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

print('''
¿Cómo podría "highway-mpg" ayudarnos a predecir el precio del automóvil?

Para este ejemplo, queremos ver cómo "highway-mpg" puede ayudarnos a
predecir el precio del automóvil. Usando regresión lineal simple, crearemos una
función lineal con "highway-mpg" como variable predictora y "price" como
variable de respuesta.

Código a ejecutar:
    X = df[['highway-mpg']]
    Y = df['price']
    # Ajustar el modelo lineal utilizando highway-mpg:
    lm.fit(X, Y)
''')
X = df[['highway-mpg']]
Y = df['price']

lm.fit(X, Y)
print("Modelo ajustado correctamente.")
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

print('''
Podemos generar una predicción:

Código a ejecutar:
    Yhat = lm.predict(X)
    print(Yhat[0:5])
''')
Yhat = lm.predict(X)
print("Salida:")
print(Yhat[0:5])
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

print('''
¿Cuál es el valor del intercepto (a)?

Código a ejecutar:
    print("El valor del intercepto (a) es: ", lm.intercept_)
''')
print("El valor del intercepto (a) es: ", lm.intercept_)
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

print('''
¿Cuál es el valor de la pendiente (b)?

Código a ejecutar:
    print("El valor de la pendiente (b) es:", lm.coef_)
''')
print("El valor de la pendiente (b) es:", lm.coef_)

print(f'''
¿Cuál es el modelo lineal estimado final que obtenemos?
Como vimos anteriormente, deberíamos obtener un modelo lineal final con la estructura:
    Yhat = a + bX

Sustituyendo los valores reales obtenidos:
    Price = {lm.intercept_:.2f} + ({lm.coef_[0]:.2f} * highway-mpg)
''')
print("-" * 70)
input("Presione Enter para continuar...")

# Pregunta 1
print("\n" + "=" * 70)
print("Pregunta #1")
print("=" * 70)
print('''
Pregunta #1 a):
Cree un objeto de regresión lineal llamado "lm1".

Código a ejecutar:
    lm1 = LinearRegression()
''')
lm1 = LinearRegression()
print("Objeto 'lm1' creado.")
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

print('''
Pregunta #1 b):
Entrene el modelo usando "engine-size" como variable independiente y "price"
como variable dependiente.

Código a ejecutar:
    X1 = df[['engine-size']]
    Y1 = df['price']
    lm1.fit(X1, Y1)
''')
X1 = df[['engine-size']]
Y1 = df['price']
lm1.fit(X1, Y1)
print("Modelo lm1 entrenado correctamente.")
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

print('''
Pregunta #1 c):
Encuentre la pendiente y el intercepto del modelo.

Código a ejecutar:
    print("El valor del intercepto (a) es: ", lm1.intercept_)
    print("El valor de la pendiente (b) es:", lm1.coef_)
''')
print("El valor del intercepto (a) es: ", lm1.intercept_)
print("El valor de la pendiente (b) es:", lm1.coef_)
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

print('''
Pregunta #1 d):
¿Cuál es la ecuación de la recta de predicción? Puede usar x y yhat o
"engine-size" y "price".

Código a ejecutar:
    Yhat = lm1.predict(X1)
    print(Yhat)
''')
Yhat = lm1.predict(X1)
print("Salida:")
print(Yhat)
print(f"\nEcuación de predicción: Price = {lm1.intercept_:.2f} + ({lm1.coef_[0]:.2f} * engine-size)")
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

# Regresión Lineal Múltiple
print("\n" + "=" * 70)
print("Regresión Lineal Múltiple")
print("=" * 70)
print('''
¿Qué pasa si queremos predecir el precio del automóvil utilizando más de una variable?

Si queremos usar más variables en nuestro modelo para predecir el precio del automóvil, podemos usar
Regresión Lineal Múltiple. La regresión lineal múltiple es muy similar a la Regresión Lineal Simple,
pero este método se utiliza para explicar la relación entre una variable de respuesta continua
(dependiente) y dos o más variables predictoras (independientes). La mayoría de los modelos de regresión
del mundo real involucran múltiples predictores. Ilustraremos la estructura utilizando cuatro
variables predictoras, pero estos resultados se generalizan a cualquier número entero:

Y: Variable de respuesta
X1: Variable predictora 1
X2: Variable predictora 2
X3: Variable predictora 3
X4: Variable predictora 4

La ecuación está dada por:
    Yhat = a + b1x1 + b2x2 + b3x3 + b4x4

De la sección anterior sabemos que otros buenos predictores del precio podrían ser:
- Horsepower (caballos de fuerza)
- Curb-weight (peso en vacío)
- Engine-size (tamaño del motor)
- Highway-mpg (millas por galón en carretera)

Desarrollemos un modelo utilizando estas variables como predictoras.

Código a ejecutar:
    Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
    # Ajustar el modelo lineal utilizando las cuatro variables mencionadas:
    lm.fit(Z, df['price'])
''')
Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]

# Ajustar el modelo lineal utilizando las cuatro variables mencionadas:
lm.fit(Z, df['price'])
print("Modelo de Regresión Lineal Múltiple entrenado.")
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

print('''
¿Cuál es el valor del intercepto (a)?

Código a ejecutar:
    print("El valor del intercepto(a) es: ", lm.intercept_)
''')
print("El valor del intercepto(a) es: ", lm.intercept_)
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

print('''
¿Cuáles son los valores de los coeficientes (b1, b2, b3, b4)?

Código a ejecutar:
    print("Los valores de los coeficientes (b1, b2, b3, b4) son:", lm.coef_)
''')
print("Los valores de los coeficientes (b1, b2, b3, b4) son:", lm.coef_)

print(f'''
¿Cuál es el modelo lineal estimado final que obtenemos?
Como vimos anteriormente, deberíamos obtener una función lineal final con la estructura:
    Yhat = a + b1x1 + b2x2 + b3x3 + b4x4

¿Cuál es la función lineal que obtenemos en este ejemplo?
Price = {lm.intercept_:.2f} + {lm.coef_[0]:.2f} * horsepower + {lm.coef_[1]:.2f} * curb-weight + {lm.coef_[2]:.2f} * engine-size + {lm.coef_[3]:.2f} * highway-mpg
''')
print("-" * 70)
input("Presione Enter para continuar...")

# Pregunta 2
print("\n" + "=" * 70)
print("Pregunta #2")
print("=" * 70)
print('''
Pregunta #2 a):
Cree y entrene un modelo de Regresión Lineal Múltiple "lm2" donde la variable
de respuesta sea "price", y las variables predictoras sean "normalized-losses" y "highway-mpg".

Código a ejecutar:
    lm2 = LinearRegression()
    lm2.fit(df[["normalized-losses", "highway-mpg"]], df["price"])
''')
lm2 = LinearRegression()
lm2.fit(df[["normalized-losses", "highway-mpg"]], df["price"])
print("Modelo lm2 creado y entrenado.")
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

print('''
Pregunta #2 b):
Encuentre los coeficientes del modelo.

Código a ejecutar:
    print("Los coeficientes del modelo lm2 son: ", lm2.coef_)
''')
print("Los coeficientes del modelo lm2 son: ", lm2.coef_)
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

# -------------------------------------------------------------------------
# SECCIÓN 2: Evaluación de Modelos Mediante Visualización
# -------------------------------------------------------------------------
print("\n" + "=" * 70)
print("2. Evaluación de Modelos Mediante Visualización")
print("=" * 70)
print('''
Ahora que hemos desarrollado algunos modelos, ¿cómo los evaluamos y elegimos el mejor?
Una forma de hacerlo es mediante la visualización.

Importar el paquete de visualización, seaborn:

Código a ejecutar:
    import seaborn as sns
''')
input("Presione Enter para importar seaborn...")
import seaborn as sns
print("seaborn importado exitosamente.")
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

print('''
Gráfico de Regresión

Cuando se trata de regresión lineal simple, una excelente manera de visualizar el ajuste
de nuestro modelo es utilizando gráficos de regresión.

Este gráfico mostrará una combinación de puntos de datos dispersos (un diagrama de dispersión)
junto con la línea de regresión lineal ajustada que atraviesa los datos. Esto nos dará
una estimación razonable de la relación entre las dos variables, la fuerza de la correlación,
así como la dirección (correlación positiva o negativa).

Visualicemos highway-mpg como variable predictora potencial del precio:

Código a ejecutar:
    width = 12
    height = 10
    plt.figure(figsize=(width, height))
    sns.regplot(x="highway-mpg", y="price", data=df)
    plt.ylim(0,)
    plt.show()

(Nota: Cierre la ventana gráfica que se abrirá para continuar con el script).
''')
input("Presione Enter para mostrar el gráfico de regresión (highway-mpg)...")
width = 12
height = 10
plt.figure(figsize=(width, height))
sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0,)
plt.show()

print('''
Podemos ver en este gráfico que el precio está correlacionado negativamente con highway-mpg,
ya que la pendiente de la regresión es negativa.

Un aspecto importante a tener en cuenta al observar un gráfico de regresión es prestar atención
a qué tan dispersos están los puntos de datos alrededor de la línea de regresión. Esto le dará
una buena indicación de la varianza de los datos y de si un modelo lineal sería el mejor ajuste o no.
Si los datos están demasiado alejados de la línea, es posible que este modelo lineal no sea el más
adecuado para estos datos.

Comparemos este gráfico con el gráfico de regresión de "peak-rpm".

Código a ejecutar:
    plt.figure(figsize=(width, height))
    sns.regplot(x="peak-rpm", y="price", data=df)
    plt.ylim(0,)
    plt.show()

(Nota: Cierre la ventana gráfica para continuar).
''')
input("Presione Enter para mostrar el gráfico de regresión (peak-rpm)...")
plt.figure(figsize=(width, height))
sns.regplot(x="peak-rpm", y="price", data=df)
plt.ylim(0,)
plt.show()

print('''
Al comparar el gráfico de regresión de "peak-rpm" y "highway-mpg", vemos que los puntos para
"highway-mpg" están mucho más cerca de la línea generada y, en promedio, disminuyen. Los puntos para
"peak-rpm" tienen mayor dispersión alrededor de la línea predicha y es mucho más difícil determinar
si los puntos disminuyen o aumentan a medida que se incrementa "peak-rpm".

Pregunta #3:
Dados los gráficos de regresión anteriores, ¿está "peak-rpm" o "highway-mpg" más fuertemente
correlacionado con "price"? Utilice el método ".corr()" para verificar su respuesta.

Código a ejecutar:
    print(df[["peak-rpm","highway-mpg","price"]].corr())
''')
print("Salida:")
print(df[["peak-rpm", "highway-mpg", "price"]].corr())
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

print('''
Gráfico de Residuos
Una buena forma de visualizar la varianza de los datos es utilizar un gráfico de residuos.

¿Qué es un residuo?
La diferencia entre el valor observado (y) y el valor predicho (Yhat) se llama residuo (e).
Cuando observamos un gráfico de regresión, el residuo es la distancia desde el punto de datos
hasta la línea de regresión ajustada.

¿Entonces qué es un gráfico de residuos?
Un gráfico de residuos es un gráfico que muestra los residuos en el eje vertical y y
la variable independiente en el eje horizontal x.

¿A qué prestamos atención al observar un gráfico de residuos?
Observamos la dispersión de los residuos:
- Si los puntos en un gráfico de residuos están distribuidos aleatoriamente alrededor del eje x,
  entonces un modelo lineal es apropiado para los datos.

¿Por qué ocurre esto? Residuos distribuidos aleatoriamente significan que la varianza es constante,
y por lo tanto el modelo lineal es un buen ajuste para estos datos.

Código a ejecutar:
    width = 12
    height = 10
    plt.figure(figsize=(width, height))
    sns.residplot(x=df['highway-mpg'], y=df['price'])
    plt.show()

(Nota: Cierre la ventana gráfica para continuar).
''')
input("Presione Enter para mostrar el gráfico de residuos...")
plt.figure(figsize=(width, height))
sns.residplot(x=df['highway-mpg'], y=df['price'])
plt.show()

print('''
¿Qué nos dice este gráfico?
Podemos ver en este gráfico de residuos que los residuos no están distribuidos aleatoriamente
alrededor del eje x, lo que nos lleva a pensar que tal vez un modelo no lineal sea más
apropiado para estos datos.
''')
print("-" * 70)
input("Presione Enter para continuar...")

print('''
Regresión Lineal Múltiple mediante Gráficos de Distribución

¿Cómo visualizamos un modelo para Regresión Lineal Múltiple? Esto se vuelve un poco más
complicado porque no se puede visualizar directamente con un gráfico de regresión o de residuos simple.

Una forma de ver el ajuste del modelo es observando el gráfico de distribución.
Podemos observar la distribución de los valores ajustados resultantes del modelo y compararla con
la distribución de los valores reales.

Primero, realicemos una predicción:

Código a ejecutar:
    Y_hat = lm.predict(Z)
''')
Y_hat = lm.predict(Z)
print("Predicciones de MLR generadas.")

print('''
Ahora graficamos la distribución:

Código a ejecutar:
    plt.figure(figsize=(width, height))
    ax1 = sns.distplot(df['price'], hist=False, color="r", label="Valor Real")
    sns.distplot(Y_hat, hist=False, color="b", label="Valores Ajustados" , ax=ax1)
    plt.title('Valores Reales vs Valores Ajustados para Precio')
    plt.xlabel('Precio (en dólares)')
    plt.ylabel('Proporción de Automóviles')
    plt.show()
    plt.close()

(Nota: Cierre la ventana gráfica para continuar).
''')
input("Presione Enter para mostrar el gráfico de distribución...")
plt.figure(figsize=(width, height))
ax1 = sns.distplot(df['price'], hist=False, color="r", label="Valor Real")
sns.distplot(Y_hat, hist=False, color="b", label="Valores Ajustados", ax=ax1)
plt.title('Valores Reales vs Valores Ajustados para Precio')
plt.xlabel('Precio (en dólares)')
plt.ylabel('Proporción de Automóviles')
plt.show()
plt.close()

print('''
Podemos ver que los valores ajustados son razonablemente cercanos a los valores reales,
ya que las dos distribuciones se superponen considerablemente. Sin embargo, definitivamente
hay margen de mejora.
''')
print("-" * 70)
input("Presione Enter para continuar...")

# -------------------------------------------------------------------------
# SECCIÓN 3: Regresión Polinómica y Tuberías (Pipelines)
# -------------------------------------------------------------------------
print("\n" + "=" * 70)
print("3. Regresión Polinómica y Tuberías")
print("=" * 70)
print('''
La regresión polinómica es un caso particular del modelo de regresión lineal general o modelos
de regresión lineal múltiple.

Obtenemos relaciones no lineales elevando al cuadrado o introduciendo términos de orden superior
de las variables predictoras.

Existen diferentes órdenes de regresión polinómica:

  Cuadrática - 2do Orden:
    Yhat = a + b1*X + b2*X²

  Cúbica - 3er Orden:
    Yhat = a + b1*X + b2*X² + b3*X³

  Orden Superior:
    Y = a + b1*X + b2*X² + b3*X³ + ...

Vimos anteriormente que un modelo lineal no proporcionaba el mejor ajuste al usar
"highway-mpg" como variable predictora. Veamos si podemos probar ajustando un
modelo polinómico a los datos en su lugar.

Utilizaremos la siguiente función para graficar los datos:
''')

def PlotPolly(model, independent_variable, dependent_variabble, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.title('Ajuste Polinómico con Matplotlib para Precio ~ Longitud')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Precio de los Automóviles')

    plt.show()
    plt.close()

print("Función PlotPolly definida.")
print('''
Obtengamos las variables:
    x = df['highway-mpg']
    y = df['price']
''')
x = df['highway-mpg']
y = df['price']

print('''
Ajustemos el polinomio usando la función polyfit, y luego usemos la función
poly1d para mostrar la función polinómica.

Código a ejecutar:
    f = np.polyfit(x, y, 3)
    p = np.poly1d(f)
    print(p)
''')
f = np.polyfit(x, y, 3)
p = np.poly1d(f)
print("Salida:")
print(p)
print("\n" + "-" * 70)
input("Presione Enter para graficar la función polinómica cúbica...")

# Graficar la función:
PlotPolly(p, x, y, 'highway-mpg')

print("Coeficientes generados con np.polyfit(x, y, 3):")
print(np.polyfit(x, y, 3))

print('''
Ya podemos ver a partir del gráfico que este modelo polinómico tiene un mejor
desempeño que el modelo lineal. Esto se debe a que la función polinómica generada
"acierta" o pasa más cerca de un mayor número de puntos de datos.
''')
print("-" * 70)
input("Presione Enter para continuar...")

# Pregunta 4
print("\n" + "=" * 70)
print("Pregunta #4")
print("=" * 70)
print('''
Cree un modelo polinómico de orden 11 con las variables x e y anteriores.

Código a ejecutar:
    f1 = np.polyfit(x, y, 11)
    p1 = np.poly1d(f1)
    print(p1)
    PlotPolly(p1, x, y, 'Highway MPG')
''')
f1 = np.polyfit(x, y, 11)
p1 = np.poly1d(f1)
print("Salida:")
print(p1)
print("\nPresione Enter para mostrar la gráfica del polinomio de orden 11...")
input()
PlotPolly(p1, x, y, 'Highway MPG')
print("-" * 70)
input("Presione Enter para continuar...")

print('''
Regresión Polinómica Multivariante con Scikit-Learn

La expresión analítica para la función polinómica multivariante se vuelve compleja.
Por ejemplo, la expresión para un polinomio de segundo orden (grado=2) con dos
variables contiene términos al cuadrado e interacciones cruzadas.

Podemos realizar una transformación polinómica sobre múltiples características.
Primero, importamos el módulo:

Código a ejecutar:
    from sklearn.preprocessing import PolynomialFeatures
''')
input("Presione Enter para importar PolynomialFeatures...")
from sklearn.preprocessing import PolynomialFeatures

print('''
Creamos un objeto PolynomialFeatures de grado 2:

Código a ejecutar:
    pr = PolynomialFeatures(degree=2)
    print(pr)
    Z_pr = pr.fit_transform(Z)
''')
pr = PolynomialFeatures(degree=2)
print("Objeto creado:")
print(pr)

Z_pr = pr.fit_transform(Z)

print("\nEn los datos originales, hay 201 muestras y 4 características:")
print("Z.shape ->", Z.shape)

print("\nTras la transformación, hay 201 muestras y 15 características:")
print("Z_pr.shape ->", Z_pr.shape)
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

print('''
Canalización (Pipeline)

Las canalizaciones de datos (pipelines) simplifican los pasos del procesamiento de datos.
Usamos el módulo Pipeline para crear una tubería. También usamos StandardScaler como un paso
en nuestra canalización.

Primero importamos los módulos en este punto del flujo:

Código a ejecutar:
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
''')
input("Presione Enter para importar Pipeline y StandardScaler...")
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

print('''
Creamos la tubería creando una lista de tuplas que incluye el nombre del modelo o
estimador y su correspondiente constructor.

Código a ejecutar:
    Input = [('scale', StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model', LinearRegression())]
    pipe = Pipeline(Input)
    print(pipe)
''')
Input = [('scale', StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model', LinearRegression())]
pipe = Pipeline(Input)
print("Salida:")
print(pipe)
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

print('''
Primero, convertimos el tipo de datos de Z a float para evitar advertencias de conversión que
pueden aparecer como resultado de que StandardScaler toma entradas float.

Luego, podemos normalizar los datos, realizar la transformación y ajustar el modelo
simultáneamente.

Código a ejecutar:
    Z = Z.astype(float)
    print(pipe.fit(Z, y))
''')
Z = Z.astype(float)
print("Salida:")
print(pipe.fit(Z, y))
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

print('''
De manera similar, podemos normalizar los datos, realizar la transformación y producir una
predicción simultáneamente.

Código a ejecutar:
    ypipe = pipe.predict(Z)
    print(ypipe[0:4])
''')
ypipe = pipe.predict(Z)
print("Salida (primeras 4 predicciones):")
print(ypipe[0:4])
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

# Pregunta 5
print("\n" + "=" * 70)
print("Pregunta #5")
print("=" * 70)
print('''
Cree una canalización que estandarice los datos y luego produzca una predicción
utilizando un modelo de regresión lineal con las características Z y el objetivo y.

Código a ejecutar:
    Input = [('scale', StandardScaler()), ('model', LinearRegression())]
    pipe = Pipeline(Input)
    pipe.fit(Z, y)
    ypipe = pipe.predict(Z)
    print(ypipe[0:10])
''')
Input = [('scale', StandardScaler()), ('model', LinearRegression())]
pipe = Pipeline(Input)
pipe.fit(Z, y)
ypipe = pipe.predict(Z)
print("Salida (primeras 10 predicciones):")
print(ypipe[0:10])
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

# -------------------------------------------------------------------------
# SECCIÓN 4: Medidas para la Evaluación en la Muestra
# -------------------------------------------------------------------------
print("\n" + "=" * 70)
print("4. Medidas para la Evaluación en la Muestra")
print("=" * 70)
print('''
Al evaluar nuestros modelos, no solo queremos visualizar los resultados, sino que también
queremos una medida cuantitativa para determinar qué tan preciso es el modelo.

Dos medidas muy importantes que se utilizan con frecuencia en estadística para determinar
la precisión de un modelo son:
  * R^2 / R-cuadrado
  * Error Cuadrático Medio (MSE)

R-cuadrado:
R-cuadrado, también conocido como coeficiente de determinación, es una medida que indica
qué tan cerca están los datos de la línea de regresión ajustada.
El valor de R-cuadrado es el porcentaje de variación de la variable de respuesta (y)
que es explicado por el modelo lineal.

Error Cuadrático Medio (MSE):
El Error Cuadrático Medio mide el promedio de los cuadrados de los errores. Es decir,
la diferencia entre el valor real (y) y el valor estimado (ŷ).

Modelo 1: Regresión Lineal Simple
Calculemos el R^2:

Código a ejecutar:
    # highway_mpg_fit
    lm.fit(X, Y)
    # Find the R^2
    print('The R-square is: ', lm.score(X, Y))
''')
lm.fit(X, Y)
print("Salida:")
print('The R-square is: ', lm.score(X, Y))

print('''
Podemos decir que ~49.659% de la variación del precio es explicada por este
modelo lineal simple.

Calculemos el MSE:
Podemos predecir la salida i.e., "yhat" usando el método predict, donde X es
la variable de entrada:

Código a ejecutar:
    Yhat = lm.predict(X)
    print('The output of the first four predicted value is: ', Yhat[0:4])
''')
Yhat = lm.predict(X)
print("Salida:")
print('The output of the first four predicted value is: ', Yhat[0:4])
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

print('''
Importemos la función mean_squared_error del módulo metrics:

Código a ejecutar:
    from sklearn.metrics import mean_squared_error
''')
from sklearn.metrics import mean_squared_error

print('''
Podemos comparar los resultados predichos con los resultados reales:

Código a ejecutar:
    mse = mean_squared_error(df['price'], Yhat)
    print('The mean square error of price and predicted value is: ', mse)
''')
mse = mean_squared_error(df['price'], Yhat)
print("Salida:")
print('The mean square error of price and predicted value is: ', mse)
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

print('''
Modelo 2: Regresión Lineal Múltiple
Calculemos el R^2:

Código a ejecutar:
    # fit the model
    lm.fit(Z, df['price'])
    # Find the R^2
    print('The R-square is: ', lm.score(Z, df['price']))
''')
lm.fit(Z, df['price'])
print("Salida:")
print('The R-square is: ', lm.score(Z, df['price']))

print('''
Podemos decir que ~80.896 % de la variación del precio es explicada por esta
regresión lineal múltiple "multi_fit".

Calculemos el MSE. Producimos una predicción:

Código a ejecutar:
    Y_predict_multifit = lm.predict(Z)
    print('The mean square error of price and predicted value using multifit is: ',
          mean_squared_error(df['price'], Y_predict_multifit))
''')
Y_predict_multifit = lm.predict(Z)
print("Salida:")
print('The mean square error of price and predicted value using multifit is: ',
      mean_squared_error(df['price'], Y_predict_multifit))
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

print('''
Modelo 3: Ajuste Polinómico
Calculemos el R^2.

Importemos la función r2_score del módulo metrics, ya que estamos usando una función diferente:

Código a ejecutar:
    from sklearn.metrics import r2_score
''')
from sklearn.metrics import r2_score

print('''
Aplicamos la función para obtener el valor de R^2:

Código a ejecutar:
    r_squared = r2_score(y, p(x))
    print('The R-square value is: ', r_squared)
''')
r_squared = r2_score(y, p(x))
print("Salida:")
print('The R-square value is: ', r_squared)

print('''
Podemos decir que ~67.419 % de la variación del precio es explicada por este
ajuste polinómico.

MSE:
También podemos calcular el MSE:

Código a ejecutar:
    print('MSE:', mean_squared_error(df['price'], p(x)))
''')
print("Salida:")
print('MSE:', mean_squared_error(df['price'], p(x)))
print("\n" + "-" * 70)
input("Presione Enter para continuar...")

# -------------------------------------------------------------------------
# SECCIÓN 5: Predicción y Toma de Decisiones
# -------------------------------------------------------------------------
print("\n" + "=" * 70)
print("5. Predicción y Toma de Decisiones")
print("=" * 70)
print('''
Predicción

En la sección anterior, entrenamos el modelo utilizando el método fit. Ahora
utilizaremos el método predict para producir una predicción.
Importamos pyplot para graficar y también usaremos algunas funciones de numpy:

Código a ejecutar:
    import matplotlib.pyplot as plt
    import numpy as np
''')
import matplotlib.pyplot as plt
import numpy as np

print('''
Crear una nueva entrada:

Código a ejecutar:
    new_input = np.arange(1, 100, 1).reshape(-1, 1)
''')
new_input = np.arange(1, 100, 1).reshape(-1, 1)

print('''
Ajustar el modelo:

Código a ejecutar:
    lm.fit(X, Y)
''')
lm.fit(X, Y)

print('''
Producir una predicción:

Código a ejecutar:
    yhat = lm.predict(new_input)
    print(yhat[0:5])
''')
yhat = lm.predict(new_input)
print("Salida:")
print(yhat[0:5])
print("\n" + "-" * 70)
input("Presione Enter para graficar la predicción continua...")

print('''
Podemos graficar los datos:

Código a ejecutar:
    plt.plot(new_input, yhat)
    plt.show()

(Nota: Cierre la ventana gráfica para continuar).
''')
plt.plot(new_input, yhat)
plt.show()

print('''
Toma de Decisiones: Determinación de un Buen Ajuste del Modelo

Ahora que hemos visualizado los diferentes modelos y generado los valores de R-cuadrado
y MSE para los ajustes, ¿cómo determinamos un buen ajuste del modelo?

* ¿Qué es un buen valor de R-cuadrado?
Al comparar modelos, el modelo con el valor de R-cuadrado más alto tiene un mejor ajuste
para los datos.

* ¿Qué es un buen MSE?
Al comparar modelos, el modelo con el menor valor de MSE tiene un mejor ajuste para
los datos.

Echemos un vistazo a los valores de los diferentes modelos:

Regresión Lineal Simple: Usando Highway-mpg como Variable Predictora del Precio.
* R-cuadrado: 0.49659118843391759
* MSE: 3.16 x 10^7

Regresión Lineal Múltiple: Usando Horsepower, Curb-weight, Engine-size y Highway-mpg como Variables Predictoras del Precio.
* R-cuadrado: 0.80896354913783497
* MSE: 1.2 x 10^7

Ajuste Polinómico: Usando Highway-mpg como Variable Predictora del Precio.
* R-cuadrado: 0.6741946663906514
* MSE: 2.05 x 10^7

Modelo Lineal Simple (SLR) vs. Ajuste Polinómico:
- MSE: Podemos ver que el Ajuste Polinómico redujo el MSE, ya que este MSE es
  menor que el del SLR.
- R-cuadrado: El R-cuadrado para el Ajuste Polinómico es mayor que el R-cuadrado
  para el SLR, por lo que el Ajuste Polinómico también incrementó notablemente el R-cuadrado.
Dado que el Ajuste Polinómico dio como resultado un menor MSE y un mayor R-cuadrado, podemos
concluir que fue un modelo de mejor ajuste que la regresión lineal simple para predecir
"price" con "highway-mpg" como variable predictora.

Regresión Lineal Múltiple (MLR) vs. Ajuste Polinómico:
- MSE: El MSE para el MLR es menor que el MSE para el Ajuste Polinómico.
- R-cuadrado: El R-cuadrado para el MLR es también mucho mayor que para el
  Ajuste Polinómico.

Conclusión:
Al comparar estos tres modelos, concluimos que el modelo MLR es el mejor modelo
para poder predecir el precio a partir de nuestro conjunto de datos. Este resultado
tiene sentido ya que tenemos 27 variables en total y sabemos que más de una de esas
variables son predictoras potenciales del precio final del vehículo.
''')
print("=" * 70)
print("FIN DEL TUTORIAL INTERACTIVO")
print("=" * 70)
