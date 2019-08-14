import time, os, base64
from flask import Flask, send_file, send_from_directory
from flask_restful import abort, Resource
from . import server

basedir = os.path.abspath(os.path.dirname(__file__))

class Ftp(Resource):
    def get(self, path):
        server.inst.logger.info('exec %s', path)
        return send_from_directory('../assets', path)

    def post(self, path):
        return ''

    def delete(self, path):
        return ''