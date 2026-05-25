import hashlib
import re
import time

# -----------------------------
# PASSWORD STRENGTH CHECKER
# -----------------------------

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score == 5:
        return "Very Strong"
    elif score >= 4:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"


# -----------------------------
# PASSWORD HASHING
# -----------------------------

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# -----------------------------
# DICTIONARY ATTACK SIMULATION
# -----------------------------

def dictionary_attack(target_hash, wordlist):
    start_time = time.time()

    for word in wordlist:
        word = word.strip()

        hashed_word = hashlib.sha256(word.encode()).hexdigest()

        if hashed_word == target_hash:
            end_time = time.time()
            return {
                "status": "Password Found",
                "password": word,
                "time_taken": round(end_time - start_time, 4)
            }

    end_time = time.time()

    return {
        "status": "Password Not Found",
        "time_taken": round(end_time - start_time, 4)
    }


# -----------------------------
# MAIN PROGRAM
# -----------------------------

print("===== PASSWORD SECURITY ANALYSIS =====\n")

password = input("Enter a password: ")

# Strength Analysis
strength = check_password_strength(password)

print("\nPassword Strength:", strength)

# Hashing
hashed = hash_password(password)

print("\nSHA-256 Hash:")
print(hashed)

# Sample Dictionary
sample_wordlist = [
    "123456",
    "password",
    "admin",
    "welcome",
    "letmein",
    "qwerty",
    "Password123",
    "hello123",
    password
]

# Dictionary Attack Simulation
print("\nRunning Dictionary Attack Simulation...\n")

result = dictionary_attack(hashed, sample_wordlist)

print("Attack Result:", result["status"])

if result["status"] == "Password Found":
    print("Recovered Password:", result["password"])

print("Time Taken:", result["time_taken"], "seconds")

# Security Suggestions
print("\n===== SECURITY RECOMMENDATIONS =====")

if strength == "Weak":
    print("- Use at least 8 characters")
    print("- Add uppercase and lowercase letters")
    print("- Include numbers and symbols")
else:
    print("- Password follows good security practices")