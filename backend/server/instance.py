from flask import Flask, Blueprint
from flask_restx import Api
import os
from dotenv import load_dotenv
load_dotenv()

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.bluePrint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.bluePrint,
                        doc='/doc',
                        title='Sample Flask Application',
                        description='A simple book api',
                        version="1.0")
        self.app.register_blueprint(self.bluePrint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['PROPAGATE_EXCEPTIONS'] = True

        self.book_ns = self.book_ns()

    def book_ns(self, ):
        return self.api.namespace(name='Books', description='book related operations', path='/')

    def run(self, ):
        self.app.run(
            port=5000,
            debug=True,
            host='0.0.0.0'
        )


server = Server()   