import time
from hashing_demo import calculate_hash


# Tries to find the password from a wordlist
def dictionary_attack(target_hash, filename="passwords.txt"):

    attempts = 0

    start_time = time.time()

    try:

        with open(filename, "r") as file:

            for line in file:

                password = line.strip()

                if not password:
                    continue

                attempts += 1

                current_hash = calculate_hash(password)

                if current_hash == target_hash:

                    end_time = time.time()

                    elapsed_time = end_time - start_time

                    return password, attempts, elapsed_time

    except FileNotFoundError:

        print("Warning: passwords.txt file not found!")

        return None, attempts, 0

    end_time = time.time()

    elapsed_time = end_time - start_time

    return None, attempts, elapsed_time


# Runs the dictionary attack
def run_dictionary_attack():

    test_password = input("\nEnter a weak password for testing: ")

    target_hash = calculate_hash(test_password)

    print("\nTarget SHA-256 Hash:")
    print(target_hash)

    print("\nStarting dictionary attack...")

    password, attempts, elapsed_time = dictionary_attack(target_hash)

    print("\n" + "=" * 45)
    print("DICTIONARY ATTACK RESULT")
    print("=" * 45)

    if password:

        print("Password Found : " + password)
        print(f"Attempts       : {attempts}")
        print(f"Elapsed Time   : {elapsed_time:.6f} seconds")

    else:

        print("Password not found in the wordlist.")
        print(f"Attempts       : {attempts}")
        print(f"Elapsed Time   : {elapsed_time:.6f} seconds")

    print("=" * 45)


if __name__ == "__main__":

    run_dictionary_attack()