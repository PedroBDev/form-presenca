from flask import Flask
import os
app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)
app.config['ADMIN_PASSWORD'] = "admin1234"

from app.routes import homepage, informacoes, admin
