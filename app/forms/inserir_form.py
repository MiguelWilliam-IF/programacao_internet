from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class InserirForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    email = StringField('Email')
    password = PasswordField('Senha')
    submit = SubmitField('Entrar')