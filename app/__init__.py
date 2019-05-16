from flask import Flask, url_for
from config import Config
import os


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    return app


from app import routes

