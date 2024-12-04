
from controllers.book import Book, BookList

def register_routes(api):
  """ Rotas de Livro """
  api.add_resource(Book, '/books/<int:id>')
  api.add_resource(BookList, '/books')


