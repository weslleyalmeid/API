from flask import render_template, flash

# ! cuidado com esse redirect e o url_for
from flask import redirect, url_for
from flask_login import logout_user

from flask_login import login_user
from app import app, db, login_manager


from app.models.tables import User
from app.models.forms import LoginForm


# * outras formas de inicializar em default
# @app.route('/index/<user>')
# @app.route('/', defaults={'user': None})
# def index(user):
#     return render_template('index.html', user=user)

@login_manager.user_loader
def load_user(id):
    # return User.query.get(user_id)
    return User.query.filter_by(id= id).first()

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route("/login", methods= ['GET','POST'])
def login():
    form  = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(username= form.username.data).first()

        if user and user.password == form.password.data:
            login_user(user)

            # ! redirecionar para o index
            return redirect(url_for("index"))
            
            flash('Logged in.') 

        else:
            flash('Invalid login.')

    return render_template('login.html', form= form)

@app.route("/teste/<info>/")
@app.route("/teste", defaults={"info": None})
def teste(info):
    i = User('almeida', '1234', 'almeida', 'almeida@hotmail.com')
    # r = User.query.filter_by(password='1234').first()
    # print(r.usarname, r.email)
    db.session.add(i)
    db.session.commit()
    return 'ok'


@app.route("/logout")
def logout():
    logout_user()
    flash('Logged out.')
    return redirect(url_for('login'))