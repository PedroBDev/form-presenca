from flask import Flask
import os
app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY")
app.config['ADMIN_PASSWORD'] = os.environ.get("ADMIN_PASSWORD")

from app.routes import homepage, informacoes, admin
