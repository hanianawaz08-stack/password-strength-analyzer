import hashlib


# Generates SHA-256 hash
def calculate_hash(text):

    hash_object = hashlib.sha256(text.encode())

    return hash_object.hexdigest()


# Demonstrates SHA-256 hashing
def hashing_demo():

    text = input("\nEnter text to hash: ")

    first_hash = calculate_hash(text)
    second_hash = calculate_hash(text)

    print("\n" + "=" * 50)
    print("SHA-256 HASHING DEMO")
    print("=" * 50)

    print(f"Input : {text}")

    print("\nFirst Hash:")
    print(first_hash)

    print("\nSecond Hash:")
    print(second_hash)

    if first_hash == second_hash:

        print("\nSame input produced the same hash.")

    else:

        print("\nUnexpected result.")

    print("=" * 50)


# Demonstrates the avalanche effect
def avalanche_demo():

    first_text = input("\nEnter original text: ")
    second_text = input("Enter slightly changed text: ")

    first_hash = calculate_hash(first_text)
    second_hash = calculate_hash(second_text)

    print("\n" + "=" * 50)
    print("AVALANCHE EFFECT DEMONSTRATION")
    print("=" * 50)

    print(f"\nOriginal Input : {first_text}")
    print(f"Original Hash  : {first_hash}")

    print(f"\nChanged Input  : {second_text}")
    print(f"Changed Hash   : {second_hash}")

    if first_hash != second_hash:

        print("\nThe hashes are completely different.")
        print("Avalanche effect demonstrated.")

    else:

        print("\nThe hashes are the same.")

    print("=" * 50)


# Tests SHA-256 hashing
def test_hashing():

    test_text = "Password123"

    hash1 = calculate_hash(test_text)

    hash2 = calculate_hash(test_text)

    if hash1 == hash2:

        print("Hash consistency test: PASSED")

    else:

        print("Hash consistency test: FAILED")


if __name__ == "__main__":

    hashing_demo()