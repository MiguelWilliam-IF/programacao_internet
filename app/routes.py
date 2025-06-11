from app import app
from flask import render_template
from app.forms.login_form import LoginForm
from app.controllers.authenticationController import AuthenticationController


@app.route("/")
def home():
    usuario = {
        'nome': 'Miguel',
        'produtos': ['banana', 'uva', 'maçã', 'salada mista']
    }

    esta_logado = True

    return render_template("index.html", usuario = None, usuario_logado = False)

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/contato")
def endereco():
    return render_template("contato.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    formulario = LoginForm()
    if formulario.validate_on_submit():
        return AuthenticationController.login(formulario)
    return render_template("login.html", title='Login', form=formulario)
