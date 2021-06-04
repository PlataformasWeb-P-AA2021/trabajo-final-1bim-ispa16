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

print("Los cantones que tiene establecimientos con 0 número de profesores")    
cantones = session.query(Canton).join(Parroquia,Establecimiento).filter(Establecimiento.docentes=='0').all()
for x in cantones:
    print(x.nombre)
    
#parte2
print("Los establecimientos que pertenecen a la parroquia Catacocha con estudiantes mayores o iguales a 21")
establecimientos = session.query(Establecimiento).join(Parroquia).filter(and_(Parroquia.nombre == 'CATACOCHA', Establecimiento.estudiantes >= '21')).all()

for x in establecimientos:
    print(x.nombre)
    '''
explicacion del any:
https://www.kite.com/python/docs/sqlalchemy.orm.RelationshipProperty.Comparator.any
matriculas = session.query(Parroquia).join(Establecimiento).filter(Establecimiento.jornada.like("Nocturna")).all()
for x in matriculas:
    print(x)
'''
