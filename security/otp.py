import pyotp

# Generate a new secret key
totp = pyotp.TOTP(pyotp.random_base32())
print("Secret:", totp.secret)

# Generate a time-based OTP
print("Your OTP:", totp.now())

# Verify OTP
otp = input("Enter OTP: ")
if totp.verify(otp):
    print("OTP is valid!")
else:
    print("Invalid OTP.")
