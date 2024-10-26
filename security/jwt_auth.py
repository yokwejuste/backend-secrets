import jwt
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv('JWT_SECRET_KEY')

def generate_jwt(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    user_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return user_token

def verify_jwt(user_token):
    try:
        payload = jwt.decode(user_token, SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

if __name__ == "__main__":
    token = generate_jwt('user123')
    print(f"Generated JWT: {token}")
    user_id = verify_jwt(token)
    print(f"Verified User ID: {user_id}")
