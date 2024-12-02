from db import db 

class ReviewModel(db.Model):
  __tablename__ = 'review'
  
  id = db.Column(db.Integer, primary_key=True)
  book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
  rating = db.Column(db.Integer, nullable=False)
  content = db.Column(db.Text, nullable=False)   
  # Definindo o relacionamento com a chave estrangeira
  book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)

  # Relacionamento inverso com Book
  book = db.relationship('BookModel', back_populates='reviews')

  def json(self,) :
    return {
      'id': self.id,
      'book_id': self.book_id,
      'rating': self.rating,
      'content': self.content
    }