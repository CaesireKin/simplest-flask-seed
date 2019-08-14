from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

inst = Flask(__name__)
apis = Api(inst)