import click

from werkzeug.security import generate_password_hash

from config import db
from models import Users


db.create_all()
admin = Users(name='Тимофей', email='bookgun@mail.ru', password=generate_password_hash('admin'), isAdmin=True)
db.session.add(admin)
db.session.commit()
