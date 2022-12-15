from main import db

class Pessoas(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    altura = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


