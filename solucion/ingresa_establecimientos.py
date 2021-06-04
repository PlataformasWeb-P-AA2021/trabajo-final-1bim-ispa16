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

#establecimientos
for dato in datos:
    dato_array = dato.split('\n');
    dato_array= dato_array[0].split('|');
    e = Establecimiento(id=dato_array[0],idParroquia= dato_array[6], nombre=dato_array[1],distrito=dato_array[8],sostenimiento =dato_array[9] ,
                        tipo = dato_array[10],modalidad = dato_array[11],jornada = dato_array[12],acceso = dato_array[13],
                        estudiantes = dato_array[14], docentes = dato_array[15])
    session.add(e)


session.commit()
