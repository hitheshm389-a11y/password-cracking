# Password Cracking and Hashing Algorithms — Project Report

**Objective**
Analyze and implement brute-force password cracking techniques while demonstrating hash functions, salting, and modern password security practices. This work is strictly for controlled lab use with test passwords you create.

**1. Background Theory**
- **Hashing:** One-way mapping from input to fixed-length output; deterministic; irreversible.
- **Salting:** Add random data per password before hashing to make identical passwords produce different hashes.

**Common Algorithms**
- MD5 — fast, insecure (legacy)
- SHA-1 — fast, insecure (legacy)
- SHA-256 — fast, suitable for hashing but not for password storage
- bcrypt / Argon2 — slow, adaptive; recommended for password storage

**Why slow hashing matters:** Fast hashes enable rapid brute-force attempts; slow/adaptive algorithms raise attack cost.

**2. Tools Used**
- **Hashcat** — GPU-accelerated cracking, many modes
- **John the Ripper** — flexible CPU tool, good for quick audits
- **Python** — scripting, generating salted hashes, and educational brute-force demos

**3. Implementation**

**Part A — Generate Hashes (Python)**
```python
import hashlib

password = "admin123"
md5_hash = hashlib.md5(password.encode()).hexdigest()
sha256_hash = hashlib.sha256(password.encode()).hexdigest()
print("MD5:", md5_hash)
print("SHA-256:", sha256_hash)
```

**Part B — Salting Example**
```python
import hashlib, os
password = "admin123"
salt = os.urandom(16)  # store salt per-user
secure_hash = hashlib.sha256(salt + password.encode()).hexdigest()
print("Salt:", salt.hex())
print("Salted Hash:", secure_hash)
```

**Part C — Simple Brute-Force Demo (Educational Only)**
```python
import hashlib, itertools, string

target_hash = hashlib.md5("abc".encode()).hexdigest()
characters = string.ascii_lowercase
max_length = 3
for length in range(1, max_length+1):
    for guess in itertools.product(characters, repeat=length):
        guess_password = ''.join(guess)
        if hashlib.md5(guess_password.encode()).hexdigest() == target_hash:
            print("Password found:", guess_password)
            raise SystemExit
```

**Part D — Hashcat (example)**
- Save the hash to `hash.txt`.
- Run: `hashcat -m 0 hash.txt ?a?a?a?a`  (-m 0 = MD5, `?a` = all chars)

**Part E — John the Ripper (example)**
- `john --format=raw-md5 hash.txt`
- `john --show hash.txt`

**4. Experiments & Analysis**
- Experiment 1: Hash Speed Comparison
  - Measure cracking time for MD5, SHA-256, and bcrypt (use cost factors for bcrypt).
  - Expected: MD5 fastest to crack; bcrypt slowest.

- Experiment 2: Password Length Impact
  - Test lengths 3, 5, 8 using the same character set; observe exponential time growth.

- Experiment 3: Salting Effect
  - Create two identical passwords, compute unsalted and salted hashes. Unsalted hashes match; salted differ.

**5. Results & Discussion**
- Fast hashes (MD5/SHA-1) are unsuitable for passwords.
- Salting prevents simple rainbow-table matches and cross-database hash leaks.
- GPU acceleration significantly reduces time for brute-force on fast hashes.
- Longer and higher-entropy passwords raise the attack cost exponentially.

**6. Security Implications & Recommendations**
- Use Argon2 or bcrypt (configurable cost) with per-user unique salts.
- Enforce password length and entropy (passphrases preferred).
- Apply rate-limiting, account lockouts, and MFA.
- For legacy migrations, re-hash with a slow algorithm on next login.

**7. Ethical & Safety Note**
Only run cracking tools against systems and hashes you own or have explicit permission to test. This project is for defensive research and education.

**8. Conclusion**
- Hashing alone is insufficient; salt + slow hashing is required.
- Password complexity and system protections (rate-limiting, MFA) are crucial.

**9. Appendix — Suggested Experiments & Commands**
- Hashcat: `hashcat -m 0 hash.txt ?a?a?a?a` (MD5)
- John: `john --format=raw-md5 hash.txt`
- Python scripts: use the provided examples and increase character sets/cost factors for tests.

**References**
- NIST Digital Identity Guidelines
- RFC 7914 (scrypt)
- bcrypt and Argon2 documentation

---
Generated for lab use. If you want, I can also:
- convert this to a PDF or Word doc,
- produce a PowerPoint outline,
- expand into a step-by-step lab manual,
- add runnable scripts and a `README.md` for a GitHub repo.
