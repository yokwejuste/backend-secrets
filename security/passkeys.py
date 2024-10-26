from flask import Flask, request, jsonify, session
from webauthn import generate_registration_options, verify_registration_response
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

users = {}


@app.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')

    registration_options = generate_registration_options(
        rp_id="localhost",
        rp_name="MyApp",
        user_id=email,
        user_name=email
    )

    session['registration_options'] = registration_options
    return jsonify(registration_options)


@app.route('/register/verify', methods=['POST'])
def verify_registration():
    email = request.json.get('email')
    response = request.json.get('response')

    registration_options = session.get('registration_options')

    try:
        verified = verify_registration_response(response, registration_options)
        users[email] = verified
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
