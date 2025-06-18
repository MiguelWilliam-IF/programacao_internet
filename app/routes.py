from app import app, db
from flask import render_template, redirect, request
from app.forms.login_form import LoginForm
from app.forms.inserir_form import InserirForm
from app.controllers.authenticationController import AuthenticationController
from app.controllers.insertController import InsertController
from app.models import Usuario

@app.route("/")
def home():
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

@app.route("/cadastro")
def cadastro():
    usuario = Usuario(username='leosilva', email='leo@leo.com')
    db.session.add(usuario)
    db.session.commit()

    return redirect('/')

@app.route("/inserir", methods=['GET', 'POST'])
def inserir():
    formulario = InserirForm()

    if formulario.validate_on_submit():
        return InsertController.cadastro(formulario)
        
    return render_template("inserir.html", title='Cadastro', form=formulario)