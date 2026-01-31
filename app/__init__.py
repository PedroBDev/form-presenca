from flask import Flask
import os
app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("FLASK_SECRET_KEY")
app.config['ADMIN_PASSWORD'] = os.getenv("ADMIN_PASSWORD")

from app.routes import homepage, informacoes, admin
