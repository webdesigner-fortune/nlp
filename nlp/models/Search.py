from nlp import db

class Search(db.Model):
    __tablename__ = 'search'
     
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.String())
   

    def __init__(self, result):
        self.result = result

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'result':self.result
        }