from flask import Flask
from databases import config

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)