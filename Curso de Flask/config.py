import os.path

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///storage.db' 
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Ajustar chave para os formulários
SECRET_KEY = 'um-nome-bem-seguro'