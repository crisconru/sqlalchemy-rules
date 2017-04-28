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

# Llenar bbdd
datos = [('Victor Suarez', 'Coding Dojo'),
         ('Miguel Angel', 'Kotlin Mola y lo sabes'),
         ('Cristo calvo', 'SQLAlchemy rules'),
         ('Juanjo Salvador', 'Como hacer tu API REST con Django en una noche'),
         ('Juan Pedro Ramos', 'Como hacer tu API REST con Django en una noche')]
query = 'INSERT INTO charla VALUES (?,?)'
cursor.executemany(query, datos)

# Ver datos en tabla
query = 'SELECT * FROM charla'
cursor.execute(query)
elementos = cursor.fetchall()
for elemento in elementos:
    print(elemento)
print('---------------------------------------------------------------------------------------------------------------')

# Escoger un dato
autor = elementos[2][0]
print('Autor mas calvo = {}'.format(autor))

# ----------------------------------------------------------------------------------------------------------------------
# Guardar la operacion
conector.commit()
# Cerrar la conexion
conector.close()
