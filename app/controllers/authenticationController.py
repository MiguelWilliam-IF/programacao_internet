from flask import render_template, flash

class AuthenticationController:

    def login(form):
        flash(f"O usuario {form.username.data} fez o login, lembrar={form.remember_me.data}")

        usuario = {
            'nome': form.username.data
        }

        return render_template('/')