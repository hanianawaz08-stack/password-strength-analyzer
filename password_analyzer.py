import math
import secrets
import string

# Generates a random secure password
def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    new_password = ""
    for i in range(length):
        new_password += secrets.choice(chars)
    return new_password


# Loads the weak passwords file
def load_common_passwords():

    common_list = []

    try:

        with open("passwords.txt", "r") as file:

            for line in file:

                password = line.strip().lower()

                if password:

                    common_list.append(password)

    except FileNotFoundError:

        print("Warning: passwords.txt file not found!")

    return common_list


# Calculates total character pool size based on types present
def get_pool_size(password):
    pool = 0
    
    # Check for lowercase
    for c in password:
        if c.islower():
            pool += 26
            break
            
    # Check for uppercase
    for c in password:
        if c.isupper():
            pool += 26
            break
            
    # Check for digits
    for c in password:
        if c.isdigit():
            pool += 10
            break
            
    # Check for symbols
    for c in password:
        if c in string.punctuation:
            pool += len(string.punctuation)
            break
            
    return pool


# Calculates bits of entropy: E = L * log2(R)
def calculate_entropy(password):
    pool_size = get_pool_size(password)
    if pool_size == 0 or len(password) == 0:
        return 0
    return len(password) * math.log2(pool_size)


# Saves basic check logs to history.txt
def save_to_history(score, entropy, strength):
    with open("history.txt", "a") as file:
        file.write(f"Score: {score}/5 | Entropy: {entropy:.2f} bits | Strength: {strength}\n")