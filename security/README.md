# Security

This folder contains various security implementations, from encryption and password hashing to secure authentication and rate limiting. Each file provides a specific security feature commonly used in backend applications, helping protect data, manage access control, and secure communications.

## Contents

- [AES Encryption](#aes-encryption)
- [Password Hashing with Bcrypt](#password-hashing-with-bcrypt)
- [CORS (Cross-Origin Resource Sharing)](#cors-cross-origin-resource-sharing)
- [CSRF Protection](#csrf-protection)
- [Flask Security Headers](#flask-security-headers)
- [Flask Rate Limiting](#flask-rate-limiting)
- [JWT Authentication](#jwt-authentication)
- [OTP (One-Time Password)](#otp-one-time-password)
- [Passkeys](#passkeys)
- [RBAC and ABAC](#rbac-and-abac)
- [Apache SSL Configuration](#apache-ssl-configuration)
- [TLS Configuration for Nginx](#tls-configuration-for-nginx)

---

### AES Encryption

**AES (Advanced Encryption Standard)** is a symmetric encryption algorithm used for securing sensitive data.

- **File**: `aes_encryption.py`
- **Setup**:
  1. Install `cryptography` library: `pip install cryptography`.

- **Example Usage**:
  ```python
  from aes_encryption import encrypt_data, decrypt_data
  encrypted = encrypt_data("my_secret_data")
  decrypted = decrypt_data(encrypted)
  ```

---

### Password Hashing with Bcrypt

**Bcrypt** is a cryptographic algorithm for hashing passwords, making them difficult to reverse.

- **File**: `bcrypt_passwords.py`
- **Setup**:
  1. Install `bcrypt` library: `pip install bcrypt`.

- **Example Usage**:
  ```python
  from bcrypt_passwords import hash_password, check_password
  hashed = hash_password("my_password")
  is_valid = check_password("my_password", hashed)
  ```

---

### CORS (Cross-Origin Resource Sharing)

**CORS** controls the domains that can access your API, adding a layer of security to prevent unauthorized cross-origin requests.

- **File**: `cors.py`

- **Example Usage**:
  ```python
  from cors import setup_cors
  setup_cors(app)
  ```

---

### CSRF Protection

**CSRF (Cross-Site Request Forgery)** prevents malicious users from making requests on behalf of other users without their consent.

- **File**: `csrf.py`

- **Example Usage**:
  ```python
  from csrf import generate_csrf_token, verify_csrf_token
  token = generate_csrf_token()
  is_valid = verify_csrf_token(token)
  ```

---

### Flask Security Headers

**Security Headers** in Flask provide an extra layer of security by adding headers to responses, protecting against vulnerabilities like clickjacking and XSS.

- **File**: `flask_headers.py`

- **Example Usage**:
  ```python
  from flask_headers import set_security_headers
  set_security_headers(app)
  ```

---

### Flask Rate Limiting

**Rate Limiting** restricts the number of requests an IP or user can make, reducing the risk of abuse and denial-of-service attacks.

- **File**: `flask_rate_limiting.py`

- **Example Usage**:
  ```python
  from flask_rate_limiting import apply_rate_limit
  apply_rate_limit(app)
  ```

---

### JWT Authentication

**JWT (JSON Web Token)** is a method of secure token-based authentication, commonly used in APIs.

- **File**: `jwt_auth.py`

- **Example Usage**:
  ```python
  from jwt_auth import create_jwt, verify_jwt
  token = create_jwt({"user_id": 123})
  is_valid = verify_jwt(token)
  ```

---

### OTP (One-Time Password)

**OTP** provides a single-use password, usually as a secondary authentication factor.

- **File**: `otp.py`

- **Example Usage**:
  ```python
  from otp import generate_otp, verify_otp
  otp_code = generate_otp()
  is_valid = verify_otp(otp_code)
  ```

---

### Passkeys

**Passkeys** offer a secure, passwordless way of authenticating users, helping prevent credential-based attacks.

- **File**: `passkeys.py`

- **Example Usage**:
  ```python
  from passkeys import create_passkey, verify_passkey
  passkey = create_passkey("user_id")
  is_valid = verify_passkey("user_id", passkey)
  ```

---

### RBAC and ABAC

**RBAC (Role-Based Access Control)** and **ABAC (Attribute-Based Access Control)** provide granular control over resource access based on user roles or attributes.

- **File**: `rbac_abac.py`

- **Example Usage**:
  ```python
  from rbac_abac import check_rbac, check_abac
  has_access = check_rbac("user_role", "resource")
  has_attr_access = check_abac({"role": "admin"}, "resource")
  ```

---

### Apache SSL Configuration

**SSL Configuration** for Apache provides secure HTTPS communication for web servers, ensuring data is encrypted between the client and server.

- **File**: `apache_setup.md`

- **Usage**:
  - This file provides instructions for setting up SSL on Apache using a Let's Encrypt certificate. Follow the steps to secure your Apache server with SSL.

---

### TLS Configuration for Nginx

**TLS Configuration** in Nginx secures communication over HTTPS and enforces best practices for strong ciphers and protocol settings.

- **File**: `tls_nginx_security.conf`
- **Usage**:
  - Configure this file in your Nginx server block to enforce strong TLS settings, improving security for your web server.

---

## How to Use

1. Clone the repository and navigate to the `security` folder.
2. Install any required dependencies as mentioned in each section.
3. Refer to each script or configuration file for setup and usage instructions.

## Contributing

Contributions are welcome! If you’d like to add more security features or enhance existing implementations, please submit a pull request with a detailed description of your changes.
