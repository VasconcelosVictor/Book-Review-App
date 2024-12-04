from flask import request
from flask_restx import Resource, fields
from models.book import BookModel
from schemas.book import BookSchema
from server.instance import server

book_ns = server.book_ns
book_schema = BookSchema()
book_list_schema = BookSchema(many=True)

ITEM_NOTFOUND = 'Book not found.'
item = book_ns.model('Book',{
  'title': fields.String(required=True, description='Book title'),
  'author': fields.String(required=True, description='Author of the book'),
  'description': fields.String(description='Book description')  
  })

class Book(Resource):
  def get(self, id):
    book_data = BookModel.find_by_id(id)
    if book_data:
      return book_schema.dump(book_data) , 200
    return {'message': ITEM_NOTFOUND} , 404
  
  @book_ns.expect(item)
  def put(self, id):
    book_data = BookModel.find_by_id(id)
    book_json = request.get_json()

    book_data.title =  book_json['title']
    book_data.author =  book_json['author']
    book_data.description =  book_json['description']

    book_data.save_to_db()

    return book_schema.dump(book_data), 200
  

  def delete(self, id):
    book_data = BookModel.find_by_id(id)
    if book_data:
      book_data.delete_from_db()
      return '', 204
    return {'message': ITEM_NOTFOUND}
  

class BookList(Resource):

  def get(self, ):
    return book_list_schema.dump(BookModel.find_all())  
  
  @book_ns.expect(item)
  @book_ns.doc('Create an Item')
  def post(self,):
      book_json = request.get_json()
      book_data = book_schema.load(book_json)

      book_data.save_to_db()

      return book_schema.dump(book_data), 201