import sqlite3

# Crear conector de la base de datos SQLite
conector = sqlite3.connect('base_de_datos.db')
# Crear cursor para trabajar con ella
cursor = conector.cursor()
# Escribir la orden -> Generar una tabla
query = 'CREATE TABLE charla (autor VARCHAR, titulo VARCHAR)'
# Ejecutar la orden
try:
    cursor.execute(query)
except sqlite3.OperationalError as e:
    print('Error creando tabla "charla" = {}'.format(e))
finally:
    # Guardar la operacion
    conector.commit()
    # Cerrar la conexion
    conector.close()
