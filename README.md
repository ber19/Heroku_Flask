# Heroku_Flask
La plataforma hecha con Flask con configuración para despliegue en Heroku.

## Pasos:
1. Crear las tablas de la aplicación:<br />
&nbsp;&nbsp;heroku run python crear_tablas.py
      
2. Crear un usuario administrador para poder entrar a la plataforma:<br />
&nbsp;&nbsp;heroku run python crear_admin.py

## Variables de entorno necesarias:
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- S3_BUCKET&nbsp;&nbsp;(el nombre del bucket)
