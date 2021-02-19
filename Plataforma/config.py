from decouple import config

SECRET_KEY = '\xf0?a\x9a\\\xff\xd4;\x0c\xcbHi'

DEBUG = False
SQLALCHEMY_DATABASE_URI = config('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False