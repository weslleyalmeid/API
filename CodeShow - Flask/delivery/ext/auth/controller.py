from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename

from flask import current_app as app

from delivery.ext.auth.models import User
from delivery.ext.db import db
import os.path

# algoritmo de autenticação
ALG = 'pbkdf2:sha256'

# utilizando type anotation
def create_user(email: str, password: str, admin: bool = False) -> User:
    # hashing da senha
    password = generate_password_hash(password, ALG)
    user = User(email=email, passwd=password, admin=admin)
    db.session.add(user)
    # todo: Tratar exception caso user já exista
    db.session.commit()
    return user

def save_user_foto(filename, filestorage):
    """
        Saves user foto in
        ./uploads/foo/ehauehau.ext
    """
    filename = os.path.join(
        app.config['UPLOAD_FOLDER'],
        secure_filename(filename)
    )
    # todo: verificar se o diretório existe
    # todo: criar o diretório
    filestorage.save(filename)

