from flask import Flask
from flask_wtf import CSRFProtect
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

csrf = CSRFProtect(app) # Protege os formulários contra ataques CSRF

from app import routes