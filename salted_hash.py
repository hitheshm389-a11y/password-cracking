import hashlib
import os

password = "admin123"
salt = os.urandom(16)  # store salt per-user
secure_hash = hashlib.sha256(salt + password.encode()).hexdigest()
print("Password:", password)
print("Salt:", salt.hex())
print("Salted SHA-256:", secure_hash)
