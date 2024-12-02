from flask import jsonify, Flask , Blueprint
from ma import ma
from db import db
from controllers.book import Book

from server.instance import server

api = server.api
app = server.app




api.add_resource(Book, '/books/<int:id>')

if __name__ == '__main__':
  db.init_app(app)
  ma.init_app(app)
  
  server.run()    
