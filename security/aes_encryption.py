from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
import os

KEY = os.getenv('AES_SECRET_KEY')[:32].encode()

def encrypt(plain_text):
    cipher = AES.new(KEY, AES.MODE_CBC)
    iv = cipher.iv
    cipher_text = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    return b64encode(iv + cipher_text).decode('utf-8')

def decrypt(cipher_text):
    cipher_text = b64decode(cipher_text)
    iv = cipher_text[:16]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    plain_text = unpad(cipher.decrypt(cipher_text[16:]), AES.block_size)
    return plain_text.decode('utf-8')

# Example usage
if __name__ == "__main__":
    encrypted = encrypt("This is a secret message")
    print(f"Encrypted: {encrypted}")
    decrypted = decrypt(encrypted)
    print(f"Decrypted: {decrypted}")
