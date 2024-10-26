from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(app)

@app.route("/")
def home():
    return "Welcome to a secure site!"

if __name__ == "__main__":
    app.run()
