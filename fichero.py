import sqlite3

# Crear conector de la base de datos SQLite
conector = sqlite3.connect('base_de_datos.db')
# Crear cursor para trabajar con ella
cursor = conector.cursor()
# Escribir la orden -> Generar una tabla
query = 'CREATE TABLE IF NOT EXISTS charla (autor VARCHAR, titulo VARCHAR)'
# Ejecutar la orden
cursor.execute(query)
# ----------------------------------------------------------------------------------------------------------------------

# Obtener un elemento
query = 'SELECT * FROM charla'
cursor.execute(query)
print(cursor.fetchone())

# ----------------------------------------------------------------------------------------------------------------------
# Guardar la operacion
conector.commit()
# Cerrar la conexion
conector.close()
