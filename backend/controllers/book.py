from flask import request
from flask_restx import Resource, fields
from models.book import BookModel
from models.review import ReviewModel
from schemas.book import BookSchema
from server.instance import server


book_ns = server.book_ns

book_schema = BookSchema()
book_list_schema = BookSchema(many=True)

class Book(Resource):
  def get(self, id):
    book_data = BookModel.find_by_id(id)
    if book_data:
      return book_schema.dump(book_data)