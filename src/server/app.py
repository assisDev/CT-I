from flask import Flask
import controllers.casoController as c
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)


app.register_blueprint(c.caso)

if __name__ == "__main__":
    app.run(debug=True)
    