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

print("Las parroquias que tienen establecimientos únicamente en la jornada Nocturna")    
parroquia = session.query(Parroquia).filter(Parroquia.establecimientos.any(jornada="Nocturna")).all()
#explicacion del any: La funcion Any realiza una subconsulta en la tabla establecimientos
#https://www.kite.com/python/docs/sqlalchemy.orm.RelationshipProperty.Comparator.any
for x in parroquia:
    print(x.nombre)
    
#parte2
print("Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459")
#numeros =[448, 450, 451, 454, 458, 459]
cantones = session.query(Canton).join(Parroquia,Establecimiento).filter(or_(Establecimiento.estudiantes == '448', Establecimiento.estudiantes == '450',
                                                                    Establecimiento.estudiantes == '451',Establecimiento.estudiantes == '454',
                                                                    Establecimiento.estudiantes == '458',Establecimiento.estudiantes == '459')).all()

for x in cantones:
    print(x.nombre)

