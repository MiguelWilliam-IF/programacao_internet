from flask import flash, redirect
from app.models.usuario import Usuario
from app import db

class InsertController:

    def cadastro(form):
        usuario = Usuario(username=form.username.data, email=form.email.data, password_hash=form.password.data)

        db.session.add(usuario)
        db.session.commit()

        flash(f"O usuario {form.username.data} fez o cadastro! Email={form.email.data}")

        return redirect('/login')