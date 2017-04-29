from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from fichero_sqlalchemy import Base, Charla

# Genero el engine
engine = create_engine('sqlite:///base_de_datos.db')
# Bindeo - asocio la bbdd (engine) con el modelo SQLAlchemy
Base.metadata.bind = engine
# Genero una sesion con la bbdd
DBSession = sessionmaker(bind=engine)
sesion = DBSession()
# ----------------------------------------------------------------------------------------------------------------------

# Llenar bbdd con una charla
charla = Charla(autor='Victor Suarez', titulo='Coding Dojo')
sesion.add(charla)

# Llenar bbdd con varias charlas
charlas = [
    Charla(autor='Miguel Angel', titulo='Kotlin Mola y lo sabes'),
    Charla(autor='Cristo calvo', titulo='SQLAlchemy rules'),
    Charla(autor='Juanjo Salvador', titulo='Como hacer tu API REST con Django en una noche'),
    Charla(autor='Juan Pedro Ramos', titulo='Como hacer tu API REST con Django en una noche')
]
sesion.add_all(charlas)

# Ver datos en tabla
datos = sesion.query(Charla).all()
for dato in datos:
    print('{}, {}'.format(dato.autor, dato.titulo))
print('---------------------------------------------------------------------------------------------------------------')

# Escoger un dato
calvo = datos[2]
print('Autor mas calvo = {}'.format(calvo.autor))

# ----------------------------------------------------------------------------------------------------------------------
# Guardar las operaciones
sesion.commit()
# Cerrar la conexion
sesion.close()
