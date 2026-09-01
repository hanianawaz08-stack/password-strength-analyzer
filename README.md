# Password Security Toolkit

This is a Python command-line project I built during my Cybersecurity Internship. The idea was to look at password security from both sides — how a defender would judge whether a password is actually strong, and how an attacker would go about breaking one if they got their hands on its hash.

Rather than just reading about concepts like entropy or the avalanche effect, I wanted to actually build something that shows them happening, so the project ended up combining a password strength checker, a hashing demo, and a small offline dictionary attack simulator, all in one CLI tool.

---

## What This Project Is Trying to Show

- How to judge password strength using practical checks, not just gut feeling
- How to estimate a password's entropy in bits
- How to check if a password shows up in a common/breached password list
- How SHA-256 hashing works in Python
- That hashing the same input twice always gives you the same result
- The avalanche effect — how changing just one character completely changes the hash
- How an offline dictionary attack actually works, step by step
- Why all of this, put together, makes the case for using strong, unpredictable passwords

---

## Features

### 1. Password Strength Analyzer
This checks a password against several criteria:

- Length
- Whether it has uppercase letters
- Whether it has lowercase letters
- Whether it has numbers
- Whether it has special characters
- Whether it's on a common/breached password list

From these checks, it works out a score out of 5, figures out the character pool size, estimates the entropy in bits, and gives an overall strength rating. If the password is weak, it also suggests how to make it better instead of just flagging it and stopping there.

### 2. Secure Password Generator
If you'd rather not think of a password yourself, the tool can generate one using a mix of letters, numbers, and special characters. It uses Python's `secrets` module for this instead of the regular `random` module, since `secrets` is built specifically for security-related randomness and isn't predictable the way `random` can be.

### 3. SHA-256 Hashing Demo
This part uses Python's `hashlib` to hash inputs with SHA-256 and shows two things clearly:

- The same input always produces the exact same hash, every time
- No matter how long or short the input is, the output hash is always the same fixed length, shown in hex

### 4. Avalanche Effect Demo
Here, two almost-identical inputs are hashed and compared side by side. For example:

```text
Password123
Password124
```

Only the last digit is different, but the two SHA-256 hashes come out looking completely unrelated to each other. That's the avalanche effect — a good hash function is supposed to react to even the smallest change in input by scrambling the entire output.

### 5. Dictionary Attack Simulator
This one ties everything together. It simulates the kind of offline attack that happens when someone steals a database of password hashes and tries to crack them without needing to log in anywhere. The flow looks like this:

```text
Test Password
      ↓
Generate SHA-256 Hash
      ↓
Read passwords.txt
      ↓
Hash Each Candidate
      ↓
Compare With Target Hash
      ↓
Match Found / Not Found
```

At the end, it reports whether the password was cracked, how many attempts it took, and how long the whole process took. Everything here runs locally, using passwords and hashes made just for this project.

---

## Project Structure

```text
password security toolkit/
│
├── main.py
├── password_analyzer.py
├── hashing_demo.py
├── dictionary_attack.py
├── passwords.txt
├── history.txt
├── README.md
└── .gitignore
```

| File | Purpose |
|---|---|
| `main.py` | Main menu that ties all the modules together |
| `password_analyzer.py` | Password analysis, entropy calculation, password generation, and history logging |
| `hashing_demo.py` | SHA-256 hashing and avalanche effect demo |
| `dictionary_attack.py` | Offline dictionary attack simulation |
| `passwords.txt` | 10,000-entry common/weak password wordlist used by the analyzer and dictionary attack simulator 
| `history.txt` | Stores non-sensitive analysis results |
| `.gitignore` | Keeps unnecessary Python-generated files out of version control |

---

## Technologies Used

- Python
- `hashlib`
- `math`
- `string`
- `secrets`
- `time`

No external packages needed — everything here runs on Python's standard library.

---

## How to Run It

Make sure Python is installed, then open a terminal in the project folder and run:

```bash
python main.py
```

You'll get a menu with these options:

```text
1. Analyze Password Strength
2. SHA-256 Hashing Demo
3. Avalanche Effect Demo
4. Dictionary Attack Simulator
5. Generate a Secure Password
6. Exit
```

---

## Example Testing

**Weak password**
Input: `123456`
The analyzer flags this as a common/weak password.

**A password with multiple character types, but still common**  
The analyzer can identify a password that satisfies several character requirements but also appears in the common/weak password wordlist. This demonstrates that character variety alone does not guarantee password security.
This shows that a password can technically tick several boxes (uppercase, lowercase, number, special character) and still be weak simply because it's a well-known password.

**SHA-256 test**
Input: `Password123`, hashed twice, gives the exact same hash both times.

**Avalanche effect test**
Original: `Password123`
Changed: `Password124`
Only one character changed, but the resulting hashes are completely different.

**Dictionary attack test**  
The simulator generates a SHA-256 hash for a test password and compares it against SHA-256 hashes of entries in the `passwords.txt` wordlist. If the password exists in the wordlist, the simulator reports the matching password, number of attempts, and elapsed time. If no match is found, it reports that the password was not found in the wordlist.
---

## Security Considerations

This project is meant purely for educational and ethical use as part of learning cybersecurity fundamentals.

The dictionary attack simulation only ever runs locally against test passwords and hashes created for this project — it doesn't touch real accounts, websites, or any system I don't own. It also avoids saving analyzed passwords in plaintext; `history.txt` only stores non-sensitive details like the score, entropy, and strength rating, never the password itself.

---

## A Note on Password Hashing in Real Systems

SHA-256 is used here because it's the algorithm the exercise called for and it's a good way to demonstrate hashing concepts clearly. That said, it's worth pointing out that in real-world password storage, plain SHA-256 on its own isn't considered good practice. Proper systems use dedicated password hashing algorithms (like bcrypt, scrypt, or Argon2) that are deliberately slow and resistant to brute-force guessing in a way that general-purpose hash functions like SHA-256 aren't.

---

## What I Learned From This

- Working with files in Python
- Writing modular, function-based code
- Building logic for password strength analysis
- Calculating character pools and entropy
- Understanding cryptographic hashing and SHA-256 specifically
- Seeing the avalanche effect in practice, not just in theory
- How offline dictionary attacks actually work
- Basic security testing habits
- Handling password-related data responsibly

---

## Author

**Hania Nawaz**
Cybersecurity Internship Track