from nlp import db

class Books(db.Model):
    __tablename__ = 'books'
     
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String())
   

    def __init__(self, book_name):
        self.book_name = book_name

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'book_name':self.book_name
        }