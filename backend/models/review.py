from db import db 


class ReviewModel(db.Model):
  __tablename__ = 'reviews'
  
  id = db.Column(db.Integer, primary_key=True)
  book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
  rating = db.Column(db.Integer, nullable=False)
  content = db.Column(db.Text, nullable=False)   




  def json(self,) :
    return {
      'id': self.id,
      'book_id': self.book_id,
      'rating': self.rating,
      'content': self.content
    }