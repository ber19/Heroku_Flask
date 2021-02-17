from Plataforma.utils import *
from Plataforma.models import *

administrador = {
    "admin" : True,
    "username" : input("Usuario: ").strip(),
    "contrasena" : passFunc(),
    "nombre" : input("Nombre: ").strip(),
    "apellidos" : input("Apellidos: ").strip(),
    "email" : valEmail(),
    "creacion" : ahora(),
    "creado_por" : "ADMIN_MASTER"
}
existe_user = Usuarios.query.filter_by(username=administrador["username"]).first()

if existe_user is None:
    usuario_admin = Usuarios(**administrador)
    db.session.add(usuario_admin)
    db.session.commit()
else:
    print("El usuario ya existe")