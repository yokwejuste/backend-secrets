import sentry_sdk
from flask import Flask

# Initialize Sentry
sentry_sdk.init(
    dsn="https://your-sentry-dsn",
    traces_sample_rate=1.0
)

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World!"


@app.route('/error')
def trigger_error():
    division_by_zero = 1 / 0
    return "Error triggered"


if __name__ == "__main__":
    app.run(debug=True)
