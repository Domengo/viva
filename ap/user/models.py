from viva.ap.sqlalchemy import db


from flask_login import UserMixin

class User(UserMixin, db.Model):
    """Table user which holds the user info
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    username = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    fullname = db.Column(db.String(50))

    def __init__(self, email, password, username, phone, fullname):
        self.email = email
        self.fullname = fullname
        self.phone = phone
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User {self.fullname}> email {self.email} phone {self.phone}'
