from flask import Blueprint, current_app, render_template, request, redirect
from delivery.ext.auth.form import UserForm
from delivery.ext.auth.controller import create_user, save_user_foto

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    print("entrei na funcao main")
    current_app.logger.debug("Entrei na funcao main")
    return render_template("index.html")


@bp.route("/sobre")
def about():
    return render_template("about.html")


@bp.route('/cadastro', methods=['GET', 'POST'])
def signup():
    form = UserForm()

    # o form já faz a validação tudo com base no form.py
    # não tem a necessidade de verificar se é POST
    if form.validate_on_submit():
        # adicionando o usuário cadastrado no banco de dados
        #* user = User(email=form.email.data, password=form.password.data) equivalente abaixo
        #* user = User()
        #* form.populate_obj(user)
        #* db.session.add(user)
        #* db.session.commit()
        
        create_user(
            email= form.email.data,
            password= form.password.data
        )
        
        foto = request.files.get('foto')
        # import ipdb; ipdb.set_trace()
        if foto:
            save_user_foto(foto.filename, foto)
        
        return redirect('/')

    # debug manual
    # if request.method == 'POST':
    #     import ipdb; ipdb.set_trace()

    return render_template('userform.html', form=form)


@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")
