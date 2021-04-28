from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Response(db.Model):
    """JSON Resonse Model"""

    __tablename__ = "responses"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(15), nullable=False)

    def serialize(self):
        """Returns a dict representation of response which we can turn into JSON"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'year': self.year,
            'color': self.color
        }

    def __repr__(self):
        return f"<Response {self.id} name={self.name} email={self.email} year={self.year} email={self.color}>"
