from app import app 
from flask_sqlalchemy import SQLAlchemy

print("Banco de dados criado")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/database.db'
db = SQLAlchemy(app)


db.create_all()

