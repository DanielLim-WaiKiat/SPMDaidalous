from config import db

class User(db.Model):
    __tablename__ = "users"

    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)
    first_name = db.Column(db.String, nullable=True)
    last_name = db.Column(db.String, nullable=True)

    
    def __init__(self, userid, username, password, email, created_at, updated_at, first_name, last_name):
        self.userid = userid
        self.username = username
        self.password = password
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at
        self.last_name = last_name
        self.first_name = first_name

    
