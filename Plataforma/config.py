import os
from decouple import config

SECRET_KEY = '\xf0?a\x9a\\\xff\xd4;\x0c\xcbHi'

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + r"\uploads"

DEBUG = False
SQLALCHEMY_DATABASE_URI = config('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False