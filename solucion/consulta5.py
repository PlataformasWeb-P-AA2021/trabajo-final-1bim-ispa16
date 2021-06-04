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

print("\n\n\nLos establecimientos ordenados por nombre de parroquia que tengan más de 20 profesores y la cadena Permanente en tipo de educación.")    
establecimientos = session.query(Establecimiento).join(Parroquia).filter(and_(Establecimiento.docentes>'20',Establecimiento.tipo.like
                                                                              ("%Permanente"))).order_by(Parroquia.nombre).all()
for x in establecimientos:
    print(x.nombre)
    
#parte2
print("\n\n\nTodos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D02.")
establecimientos = session.query(Establecimiento).filter(Establecimiento.distrito=='11D02').order_by(Establecimiento.sostenimiento).all()

for x in establecimientos:
    print(x.nombre)
