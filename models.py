from flask_login import UserMixin

from config import db, maneger



class Users(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	email = db.Column(db.String(100), unique=False)
	password = db.Column(db.String(500), nullable=False)
	isAdmin = db.Column(db.Boolean, nullable=False)
	trustFunds = db.Column(db.PickleType, nullable=True)
	isHavePlace = db.Column(db.Boolean, nullable=True)
	bankAccount = db.Column(db.String(255), nullable=True)
	cardNumber = db.Column(db.String(255), nullable=True)
	cardDate = db.Column(db.String(15), nullable=True)
	cardCVV = db.Column(db.String(3), nullable=True)


	def __repr__(self):
		return f"<users {self.id}>"

@maneger.user_loader
def load_user(user_id):
	return Users.query.get(user_id)


class Fund(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	fundName = db.Column(db.String(50), unique=True)
	fundDiscrib = db.Column(db.Text, nullable=True)
	fundLink = db.Column(db.String(500), nullable=True)
	fundImageLink = db.Column(db.String(500),nullable=True)


	def __repr__(self):
		return f"<funds {self.id}>"

