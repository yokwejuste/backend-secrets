from flask import Flask

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)


@app.route("/api")
@limiter.limit("5 per minute")
def my_api():
    return "API response"


if __name__ == "__main__":
    app.run()
