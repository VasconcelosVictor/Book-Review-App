from db import db
from sqlalchemy.orm import relationship

class BookModel(db.Model):
  __tablename__ = 'books'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  author = db.Column(db.String(100), nullable=False)
  description = db.Column(db.Text, nullable=True)
  reviews = db.relationship('ReviewModel', back_populates='book')

  def json(self, ):
    return {
      'id': self.id,
      'title': self.title,
      'author': self.author,
      'description': self.description,
      'reviews' : self.reviews
    }
  
  @classmethod
  def find_by_title(cls, title):
    return cls.query.filter_by(title=title).first()
  
  @classmethod
  def find_by_id(cls, id):
    return cls.query.filter_by(id=id).first()
  
  @classmethod
  def find_all(cls):
    return cls.query.all()
  
  def save_to_db(self,):
    db.session.add(self)
    db.session.commit()

  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()    