# Password Checking Functions 
import random
import string


def generate_password(length):

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

def save_history(password, score):

    print("Saving history...")
    file = open("history.txt", "a")
    file.write(f"Password: {password} | Score: {score}/5\n")
    file.close()

def crack_time(score):

    if score == 5:
        return "Hundreds of years"

    elif score == 4:
        return "Several years"

    elif score == 3:
        return "Several months"

    elif score == 2:
        return "Several days"

    else:
        return "A few minutes"

common_passwords = [

    "123456",
    "12345678",
    "password",
    "password123",
    "admin",
    "admin123",
    "qwerty",
    "abc123",
    "welcome",
    "letmein",
    "iloveyou",
    "pakistan",
    "pakistan123",
    "football",
    "computer"

]

def check_common_password(password):

    if password.lower() in common_passwords:
        return True

    return False

def check_length(password):

    if len(password) >= 8:
        return True
    else:
        return False
    
def check_uppercase(password):

    for char in password:

        if char.isupper():
            return True

    return False

def check_lowercase(password):

    for char in password:

        if char.islower():
            return True

    return False
def check_numbers(password):

    for char in password:

        if char.isdigit():
            return True

    return False

def check_special_characters(password):

    special_characters = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/"

    for char in password:

        if char in special_characters:
            return True

    return False
def calculate_score(length, upper, lower, number, special):

    score = 0

    if length:
        score += 1

    if upper:
        score += 1

    if lower:
        score += 1

    if number:
        score += 1

    if special:
        score += 1

    return score

def estimate_entropy(score):

    if score == 5:
        return "Very Secure"

    elif score == 4:
        return "Secure"

    elif score == 3:
        return "Moderate"

    elif score == 2:
        return "Easy to Guess"

    else:
        return "Very Easy to Guess"

def strength_bar(score):

    if score == 5:
        return "[██████████] 100%"

    elif score == 4:
        return "[████████░░] 80%"

    elif score == 3:
        return "[██████░░░░] 60%"

    elif score == 2:
        return "[████░░░░░░] 40%"

    elif score == 1:
        return "[██░░░░░░░░] 20%"

    else:
        return "[░░░░░░░░░░] 0%"
    
