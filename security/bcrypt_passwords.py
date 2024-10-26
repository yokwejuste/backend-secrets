import bcrypt

def hash_password(user_password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(user_password.encode('utf-8'), salt)
    return hashed_password

def verify_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password)

# Example usage
if __name__ == "__main__":
    password = "SecurePass123"
    hashed = hash_password(password)
    print(f"Hashed Password: {hashed}")
    print(f"Password Verified: {verify_password(hashed, 'SecurePass123')}")
