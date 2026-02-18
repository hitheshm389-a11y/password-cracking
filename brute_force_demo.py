import hashlib
import itertools
import string

# Educational brute-force demo — only run against test hashes you own
target_hash = hashlib.md5("abc".encode()).hexdigest()
characters = string.ascii_lowercase
max_length = 3
print("Target hash (md5 of 'abc'):", target_hash)
for length in range(1, max_length+1):
    for guess in itertools.product(characters, repeat=length):
        guess_password = ''.join(guess)
        if hashlib.md5(guess_password.encode()).hexdigest() == target_hash:
            print("Password found:", guess_password)
            raise SystemExit
print("Password not found within length", max_length)
