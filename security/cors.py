from flask import Flask
from flask_cors import CORS
from starlette.middleware.cors import CORSMiddleware

app = Flask(__name__)
CORS(
    app,
    middleware=CORSMiddleware,
    resources={
        r"/api/*": {
            "origins": "https://your-allowed-origin.com",
            "methods": ["GET", "POST"],
        }
    }
)


@app.route('/api/data')
def api_data():
    return {"data": "This is secure data"}


if __name__ == "__main__":
    app.run()
