from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Modelo de clase para las tablas en SQLAlchemy
Base = declarative_base()


# Tabla charla
class Charla(Base):
    __tablename__ = 'charla'
    id = Column(Integer, primary_key=True)
    autor = Column(String(250), unique=True)
    titulo = Column(String(250))


# Crear engine de la base de datos SQLite
engine = create_engine('sqlite:///base_de_datos.db')

# Crear la base de datos y todas sus tablas
Base.metadata.create_all(engine)
