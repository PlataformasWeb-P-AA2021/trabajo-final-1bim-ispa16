# Trabajo Final Primer Bimestre

## Uso de SqlAlchemy en Windows
<img src="https://miro.medium.com/max/590/1*gJO7yKfLFOK2zfHaFDMdgA.jpeg" alt="Girl in a jacket" >


Haciendo uso de la información de la carpeta ***data***. Se realizaron las siguientes tareas:

* Analizar el contenido
	<br>**Para tener un mejor analisis de los datos se importo el archivo a una hoja de excell**		
* Identificar las posibles entidades que se puedan generar
	<br>**Se identificaron 4 entidades: Establecimientos, Provincias, Cantones, Parroquias**
* Las entidades deben satisfacer lo siguiente:
	* Un establecimiento tiene características propias.
		<br>**Las características son: id,nombre,distrito,sostenimiento,tipo ,modalidad, jornada, acceso, estudiantes, docentes**
	* Un establecimiento pertenece a una parroquia.
		<br>**Tiene una relacion de uno a muchos**
	* Una parroquia pertence a un cantón.
		<br>**Tiene una relacion de uno a uno**
	* Un cantón pertence a un provincia.
		<br>**Tiene una relacion de uno a uno**

* Generar un proceso de generación de entidades a través de SqlAlchemy. Usar Sqlite
	* genera_tablas.py
		<br>**En este archivo se realizo la creacion de las entidades, primero se creo la tabla provincia despues canton, parroquia y por ultimo la tabla establecimientos, se crearon las respectivas llaves primarias y foraneas y las relaciones usando la funcion "relationship".**

	* Ingresar la información en cada entidad creada.
		<br>**Se realizo la la lectura del archivo se limpiaron los datos y se ingresaron**
	* ingresa_provincias.py
		<br>**Se realizo la lectura del csv, se elimino el encabezado, se eliminaron los duplicados y se crearon los obejetos**
	* ingresa_cantones.py
		<br>**Se realizo la lectura del csv, se elimino el encabezado, se eliminaron los duplicados y se crearon los obejetos**
	* ingresa_parroquias.py
		<br>**Se realizo la lectura del csv, se elimino el encabezado, se eliminaron los duplicados y se crearon los obejetos**
	* ingresa_establecimientos.py
		<br>**Se realizo la lectura del csv, se elimino el encabezado y se crearon los obejetos**
* Generar las siguientes consultas:
	* consulta1.py
		* Todos los establecimientos de la provincia de Loja.
			<br>**Se selecciona la tabla Establecimiento y se filtra donde el Establecimiento.idProvincia sea igual a 7(id de la provincia de Loja)**
		* Todos los establecimientos del cantón de Loja.
			<br>**Se selecciona la tabla Establecimiento y se filtra donde el Establecimiento.idCanton sea igual a 1101(id del canton Loja)**
	* consulta2.py
    		* Las parroquias que tienen establecimientos únicamente en la jornada Nocturna
    			<br>**Se selecciona la tabla Parroquia y se filtra donde los establecimientos de la parroquia tengan jornada nocturna(se hace uso de la funcion any para hacer 	una subconsulta sobre el objeto establecimento)**
		* Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459
			<br>**Se selecciona la tabla Canton, la relacionamos con la tabla Establecimiento haciendo uso de la funcion "join" y realizamos el filtro donde 					Establecimiento.estudiantes sea igual a los numeros 448, 450, 451, 454, 458, 459  (aplicamos la	funcion "or_" para comparar todos los numeros)**
	* consulta3.py
		* Los cantones que tiene establecimientos con 0 número de profesores
			<br>**Se selecciona la tabla Establecimientos, la relacionamos con la tabla Canton haciendo uso de la funcion "join" y realizamos el filtro donde 					Establecimiento.docentes sea igual a 0**
		* Los establecimientos que pertenecen a la parroquia Catacocha con estudiantes mayores o iguales a 21
			<br>**Se selecciona la tabla Establecimientos, la relacionamos con la tabla Parroquia haciendo uso de la funcion "join" y realizamos el filtro donde 					Parroquia.nombre sea igual a Catacocha y que Establecimiento.estudiantes sea >=21  (aplicamos la funcion "and_" para aplicar las dos condiciones)**
	* consulta4.py
		* Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores. 
			<br>**Se selecciona la tabla Establecimientos y realizamos el filtro donde Establecimiento.docentes sea mayor a 100 y usamos la funcion "orderBy" para ordenar 	los resultados segun Establecimiento.estudiantes**
		* Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores.
			<br>**Se selecciona la tabla Establecimientos y realizamos el filtro donde Establecimiento.docentes sea mayor a 100 y usamos la funcion "orderBy" para ordenar los resultados segun Establecimiento.docentes**
	* consulta5.py
		* Los establecimientos ordenados por nombre de parroquia que tengan más de 20 profesores y la cadena "Permanente" en tipo de educación.
			<br>**Se selecciona la tabla Establecimientos, la relacionamos con la tabla Parroquia haciendo uso de la funcion "join" y realizamos el filtro donde 					Establecimiento.docentes sea mayor a 20 y que Establecimiento.tipo tenga la palabra "Permanente",usamos la funcion "orderBy" para ordenar 			 		los resultados segun Parroquia.nombre (aplicamos la funcion "and_" para aplicar las dos condiciones y la funcion like con los porcentajes para verificar que el nombre contenga la palabra "Permanente")**
		* Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D02.
			<br>**Se selecciona la tabla Establecimientos y realizamos el filtro donde Establecimiento.distrito sea11D02 y usamos la funcion "orderBy" para ordenar 			 	los resultados segun Establecimiento.sostenimiento**
			
## Instalacion 
#### Clonar Repositorio
```bash
git clone https://github.com/ColorlibHQ/AdminLTE.git
```
## Crear Tablas
#### En la carpeta solucion
```bash
py genera_tablas.py
```
## Ingresa Datos
#### poblar provincias
```bash
py ingresa_provincias.py
```
#### poblar cantones
```bash
py ingresa_cantones.py
```
#### poblar parroquias
```bash
py ingresa_parroquias.py
```
#### poblar establecimientos
```bash
py ingresa_establecimientos.py
```
## Generar Consultas
#### Consulta 1
```bash
py consulta1.py
```
#### Consulta 2
```bash
py consulta2.py
```
#### Consulta 3
```bash
py consulta3.py
```
#### Consulta 4
```bash
py consulta4.py
```
#### Consulta 5
```bash
py consulta5.py
```

		
