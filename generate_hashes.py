import hashlib

password = "admin123"
md5_hash = hashlib.md5(password.encode()).hexdigest()
sha256_hash = hashlib.sha256(password.encode()).hexdigest()
print("Password:", password)
print("MD5:", md5_hash)
print("SHA-256:", sha256_hash)
