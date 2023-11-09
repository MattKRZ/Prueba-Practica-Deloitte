Prueba de aplicación web para la postulación a la empresa Deloitte
----------------------------------------------------
# ¿Qué puede hacer la aplicación?
Se puede visualizar, crear, modificar y eliminar productos. Cuenta con las validaciones respectivas para usuarios que se encuentran login o logout. 
De ser necesario el código podrá ir escalando para completar sus adicionales.

## ¡Importante!
Para el completo funcionamiento de la aplicación web se debe realizar la instalación de las
siguientes dependencias que agregaré posteriormente. Toda la instalación de la dependencia se utiliza el comando pip install

### Dependencias
Las siguientes dependencias estarán asignadas con la versión con la que fue desarrollada la aplicación
1. python3 (3.12.0)
2. django-admin (4.2.7)
3. psycopg2

## ¿Cómo ejecutar la aplicación web?
1. Clonar y acceder al repositorio.
2. Configurar el motor de base de datos en settings.py
3. Cargar migración de los modelos (python3 manage.py makemigrations)
4. Migrar los modelos (python3 manage.py migrate)
5. Ejecutar la aplicación web (python3 manage.py runserver)

### ¿Cómo acceder con cuenta de administrador?
Para acceder con cuenta de administrador se debe generar con el comando "python3 manage.py createsuperuser" y rellenar los campos.

## Tecnologías utilizadas
Frontend: HTML5, CSS3 (Bootstrap) y JS.
Backend: Python (Django) y PostgreSQL.

Aplicación desarrolada por Matia Zambelli Corral, contacto: matia.zambelli@sansano.usm.cl
