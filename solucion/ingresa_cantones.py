from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import *

import json

# obtener informacion del archivo 
from configuracion import cadena_base_datos

#conectar a la base de datos
engine = create_engine(cadena_base_datos)
array =[]
result =[]
Session = sessionmaker(bind=engine)
session = Session()
# leer archivo con instituciones
datos = open("data/Listado-Instituciones-Educativas.csv", "r", encoding="utf-8")
datos = datos.readlines()[1:]#no leer encabezado

#cantones
#Tratar datos de y registrarlos
for dato in datos:
    dato_array = dato.split('\n');
    dato_array= dato_array[0].split('|');
    array.append([dato_array[4],dato_array[5],dato_array[2]])
# eliminar duplicados
for x in array:
    if x not in result:
        result.append(x)
for x in result:
    c = Canton(id=x[0], nombre=x[1], id_provincia= x[2])
    session.add(c)
session.commit()
