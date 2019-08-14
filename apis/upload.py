import time, os, base64

from flask import Flask, send_file, send_from_directory, request, jsonify
from flask_restful import abort, reqparse, Resource
from werkzeug import datastructures

from . import server

const_base_dir = 'assets/'

class Ftp(Resource):
    def get(self, path):
        server.inst.logger.debug('client try to read file: %s', path)
        return send_from_directory('assets', path)

    def post(self, path):
        server.inst.logger.debug('client post new path: %s', path)
        server.inst.logger.debug('%s', os.path.abspath(os.curdir))
        # if upload path not exist, make it
        if False == os.path.exists(const_base_dir + path):
            os.makedirs(const_base_dir + path)

        # get file and save it to the specified dir
        postFile = request.files['file']
        server.inst.logger.debug('%s', postFile)
        postFile.save(const_base_dir + path + '/' + postFile.filename)

        # return the file relative-path to the client
        url = const_base_dir + path + '/' + postFile.filename
        server.inst.logger.debug(os.path.abspath(url))
        return url

    def delete(self, path):
        success = False
        if True == os.path.exist(const_base_dir + path):
            os.remove(const_base_dir + path)
            success = true

        return success