from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Provincia,Canton,Parroquia,Establecimiento

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#parte1
estabelcimiento = session.query(Establecimiento).filter(Establecimiento.idProvincia.like("7")).all()
print("Todos los establecimientos de la provincia de Loja *****************************************")
for x in estabelcimiento:
    print(x.nombre)

#parte2
estabelcimiento = session.query(Establecimiento).filter(Establecimiento.idCanton.like("1101")).all()
print("Todos los establecimientos del canton Loja ********************************************************************************************************")
for x in estabelcimiento:
    print(x.nombre)

