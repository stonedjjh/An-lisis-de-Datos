# 5. Acceso a Bases de Datos desde Python

Las bases de datos son una herramienta fundamental para los científicos de datos. Muchas veces, los datos no estarán en simples archivos CSV o Excel, sino almacenados en potentes Sistemas de Gestión de Bases de Datos Relacionales (RDBMS).

Para conectarnos y manipular bases de datos desde un entorno de Python (como un Jupyter Notebook), utilizamos **APIs (Interfaces de Programación de Aplicaciones)**. Una API no es más que un conjunto de funciones y métodos preconstruidos que puedes llamar para acceder a un servicio determinado, en este caso, una base de datos.

## Python DB-API
DB-API es el estándar oficial de Python para acceder a bases de datos relacionales. La gran ventaja de este estándar es que **te permite escribir un único código que funciona con múltiples motores de bases de datos** (MySQL, PostgreSQL, SQLite, etc.) en lugar de tener que escribir un programa totalmente distinto para cada uno.

Si aprendes los conceptos de la DB-API, podrás aplicarlos en cualquier base de datos.

Existen dos conceptos principales en la DB-API de Python:

### 1. Objetos de Conexión (Connection Objects)
Sirven para conectarte a la base de datos y gestionar transacciones completas. Sus métodos más comunes son:
-   `cursor()`: Devuelve un nuevo objeto de cursor utilizando la conexión.
-   `commit()`: Se usa para confirmar (guardar permanentemente) cualquier transacción pendiente.
-   `rollback()`: Deshace cualquier transacción pendiente y devuelve la base de datos a su estado anterior.
-   `close()`: Se utiliza para cerrar de forma segura la conexión con la base de datos.

### 2. Objetos de Cursor (Cursor Objects)
Se utilizan para ejecutar las sentencias SQL. Funcionan de forma similar a un cursor en un procesador de texto: te permiten "desplazarte" por el conjunto de resultados y extraer los datos hacia tu aplicación Python.
- Principalmente se usan para enviar instrucciones `SQL` al motor y usar métodos como `fetch()` para extraer y traer la respuesta resultante al código.

---

## Flujo de Trabajo Típico

Al programar una conexión a base de datos en Python, el flujo normal a seguir es:

1.  **Importar el Módulo:** Importas la librería específica para tu base de datos (por ejemplo, `sqlite3` o `psycopg2`).
2.  **Abrir la Conexión (`connect`):** Llamas a la función de conexión pasándole los parámetros requeridos (nombre de la base de datos, usuario y contraseña). Esto te devuelve un "Connection Object".
3.  **Crear el Cursor:** A partir del objeto de conexión, generas un "Cursor Object".
4.  **Ejecutar Consultas (Queries):** Utilizas el cursor para mandar tus sentencias SQL (como un `SELECT * FROM tabla`).
5.  **Extraer Resultados (`fetch`):** Usas el mismo cursor para traer los resultados de la consulta a variables en tu código Python.
6.  **Cerrar la Conexión (`close`):** Finalmente, cuando terminas tus tareas, debes **siempre cerrar la conexión** utilizando la función `close()` en el objeto de conexión. De lo contrario, puedes agotar los recursos del servidor y bloquear la base de datos.
