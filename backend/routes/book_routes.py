
from controllers.book import Book

def register_routes(api):
  """ Rotas de Livro """
  api.add_resource(Book, '/books/<int:id>')


