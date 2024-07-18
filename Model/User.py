from Database_config import db_init as db


class User(db.Model):
    __tablename__ = 'user'
    username = db.Column(db.String(255), primary_key=True, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'gender': self.gender,
            'password': self.password
        }

