# Prueba - VGH

Coleccion: https://www.getpostman.com/collections/e0e31dcc4b491b12560c


## Pasos

1.- Crear un entorno virtual
- python3 -m venv Vent_Prueba
- source myvenv/bin/activate

2.- Descarga los requerimientos
- pip install -r requirements.txt

3.- Crea los modelos
- python manage.py makemigrations
- python manage.py migrate

4.- Inicia el sevicio
- python manage.py runserver 0.0.0.0:8080

5.- Crea un superusuario
- python manage.py createsuperuser

6.- Accede a el enlace

**Para la coleccion necesita un token:
- Inicia sesion con el apartado "login", en la coleccion
- Retornara un token, el cual debera anexar en las peticiones de
POST, DELETE, PUT, GET

#Bibliotecas:

-django-extensions
Se usaria frecuentemente, para la ejecucion de scripts

-django-cors-headers
Agrega encabezados de intercambio de recursos (CORS)

-psycopg2-binary
Para el uso de la base de datos postgresql

-djangorestframework
Para la creacion de las apis

-pyjwt
Para el encriptado del token

-django-rest-registration
Uso del registro, token, inicio de sesion.
