from flask import Flask
from flask_restplus import Api, Resource

flask_app = Flask(__name__)
app = Api(app=flask_app)

name_space = app.namespace("main", description="Main APIs")


def world():
    pass


def hello():
    print("hwllo world")  # blob asdf


hello()
