from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

#se va creando las tablas principales primero
class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    #se relaciona el objeto provincia con canton
    #el nombre de la tabla a relacionar, y el campo de relacion
    cantones = relationship("Canton", back_populates="provincia")
    
    def __repr__(self):
        return "Provincia: nombre=%s " % (
                          self.nombre)
class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    #se agrega la clave foranea
    id_provincia = Column(Integer, ForeignKey('provincia.id'))
    #se hacen las relaciones
    provincia = relationship("Provincia", back_populates="cantones")
    parroquias = relationship("Parroquia", back_populates="canton")    
    
    def __repr__(self):
        return "Canton: nombre=%s " % (
                          self.nombre)
class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    # se agrega la clave foranea
    id_canton = Column(Integer, ForeignKey('canton.id'))
    # se hacen las relaciones
    canton = relationship("Canton", back_populates="parroquias")
    establecimientos = relationship("Establecimiento", back_populates="parroquia")
    
    def __repr__(self):
        return "Parroquia: nombre=%s " % (
                          self.nombre)


class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    id = Column(String(100), primary_key=True)
    nombre = Column(String(100), nullable=False)
    # se agregan las claves foraneas
    idProvincia = Column(Integer, ForeignKey('provincia.id'))
    idCanton = Column(Integer, ForeignKey('canton.id'))
    idParroquia = Column(Integer, ForeignKey('parroquia.id'))
    distrito = Column(String(100), nullable=False)
    sostenimiento = Column(String(100), nullable=False)
    tipo = Column(String(100), nullable=False)
    modalidad = Column(String(100), nullable=False)
    jornada = Column(String(100), nullable=False)
    acceso = Column(String(100), nullable=False)
    estudiantes = Column(Integer, nullable=False)
    docentes = Column(Integer, nullable=False)
    # se hace la relacion
    parroquia = relationship("Parroquia", back_populates="establecimientos")
    def __repr__(self):
        return "nombre: %s - estudiantes:%d - docentes: %s" % (
                self.nombre, self.estudiantes, self.docentes)

Base.metadata.create_all(engine)
