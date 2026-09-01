import string
import password_analyzer as analyzer
import hashing_demo
import dictionary_attack


def analyze_password():

    pwd = input("\nEnter password to analyze: ")

    # Check password characteristics

    has_length = len(pwd) >= 8
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in pwd:

        if char.isupper():
            has_upper = True

        if char.islower():
            has_lower = True

        if char.isdigit():
            has_digit = True

        if char in string.punctuation:
            has_special = True

    # Check common passwords list

    common_passwords = analyzer.load_common_passwords()
    is_common = pwd.lower() in common_passwords

    # Calculate score out of 5

    score = 0

    if has_length:
        score += 1

    if has_upper:
        score += 1

    if has_lower:
        score += 1

    if has_digit:
        score += 1

    if has_special:
        score += 1

    # Calculate entropy

    entropy = analyzer.calculate_entropy(pwd)
    pool_size = analyzer.get_pool_size(pwd)

    # Determine password strength

    if is_common:

        strength = "Very Weak (Breached/Common Password)"

    elif score == 5:

        strength = "Very Strong"

    elif score == 4:

        strength = "Strong"

    elif score == 3:

        strength = "Medium"

    elif score == 2:

        strength = "Weak"

    else:

        strength = "Very Weak"

    # Save analysis results

    analyzer.save_to_history(score, entropy, strength)

    # Display password report

    print("\n" + "=" * 45)
    print("       PASSWORD SECURITY REPORT")
    print("=" * 45)

    print(f"Password Length     : {len(pwd)}")
    print(f"At least 8 chars    : {'Yes' if has_length else 'No'}")
    print(f"Has Uppercase       : {'Yes' if has_upper else 'No'}")
    print(f"Has Lowercase       : {'Yes' if has_lower else 'No'}")
    print(f"Has Numbers         : {'Yes' if has_digit else 'No'}")
    print(f"Has Special Chars   : {'Yes' if has_special else 'No'}")
    print(f"Found in Breach List: {'YES!' if is_common else 'No'}")

    print("-" * 45)

    print(f"Character Pool Size : {pool_size}")
    print(f"Estimated Entropy   : {entropy:.2f} bits")
    print(f"Final Score         : {score}/5")
    print(f"Overall Strength    : {strength}")

    print("=" * 45)

    # Suggestions for improving the password

    print("\nTips to Improve:")

    if not has_length:
        print("- Make your password longer (at least 8 characters).")

    if not has_upper:
        print("- Add some capital letters.")

    if not has_lower:
        print("- Add some small letters.")

    if not has_digit:
        print("- Include at least one number.")

    if not has_special:
        print("- Add special symbols like @, #, or !.")

    if is_common:
        print("- WARNING: This password is very common! Pick something more unique.")

    if score == 5 and not is_common:
        print("- Great job! Your password looks good.")


def generate_menu_option():

    user_input = input("\nEnter desired password length: ")

    if user_input.isdigit():

        length = int(user_input)

        if length >= 8:

            new_pwd = analyzer.generate_password(length)

            print("\nYour generated password:")
            print(new_pwd)

        else:

            print("Length should be at least 8 characters!")

    else:

        print("Please enter a valid number.")


def main():

    while True:

        print("\n" + "=" * 45)
        print("       PASSWORD SECURITY TOOLKIT")
        print("=" * 45)

        print("1. Analyze Password Strength")
        print("2. SHA-256 Hashing Demo")
        print("3. Avalanche Effect Demo")
        print("4. Dictionary Attack Simulator")
        print("5. Generate a Secure Password")
        print("6. Exit")

        choice = input("\nSelect an option (1-6): ").strip()

        if choice == "1":

            analyze_password()

        elif choice == "2":

            hashing_demo.hashing_demo()

        elif choice == "3":

            hashing_demo.avalanche_demo()

        elif choice == "4":

            dictionary_attack.run_dictionary_attack()

        elif choice == "5":

            generate_menu_option()

        elif choice == "6":

            print("\nExiting Password Security Toolkit.")
            print("Thank you for using the tool!")

            break

        else:

            print("\nInvalid input, please try again.")


if __name__ == "__main__":

    main()