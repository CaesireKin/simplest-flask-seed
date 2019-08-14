from flask_restful import Resource

from apis import server
from apis.upload import Ftp


class Index(Resource):
    def get(self):
        server.inst.logger.debug('exec')
        return 'Server is running...'

server.apis.add_resource(Index, '/')
server.apis.add_resource(Ftp, '/files/<path>')

if __name__ == "__main__":
    server.inst.run(host="0.0.0.0", port=5000, debug=True)