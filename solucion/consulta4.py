from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and
from sqlalchemy import or_
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

print("\n\n\nLos establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores.")    
establecimientos = session.query(Establecimiento).filter(Establecimiento.docentes>'100').order_by(Establecimiento.estudiantes).all()
for x in establecimientos:
    print(x.nombre)
    
#parte2
print("\n\n\nLos establecimientos ordenados por número de profesores; que tengan más de 100 profesores.")
establecimientos = session.query(Establecimiento).filter(Establecimiento.docentes>'100').order_by(Establecimiento.docentes).all()

for x in establecimientos:
    print(x.nombre)
