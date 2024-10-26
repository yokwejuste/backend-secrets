1. **Docker Compose**: Sentry can also be self-hosted with Docker Compose, but here we’ll focus on integrating Sentry with Python.

2. **Python Code**: Use the `sentry-sdk` to capture errors.

   **sentry_example.py**
   ```python
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
   ```

#### Process
1. Run `sentry_example.py` and navigate to `http://localhost:5000/error` to trigger an error.
2. Verify that the error appears in your Sentry project dashboard.
