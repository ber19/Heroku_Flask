from Plataforma.app import db
from Plataforma.models import *

db.drop_all()
db.create_all()