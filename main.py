# ==========================================
# Password Strength Analyzer
# Author: Hania Tul Maria
# ==========================================

from checker import (
    check_length,
    check_uppercase,
    check_lowercase,
    check_numbers,
    check_special_characters,
    check_common_password,
    calculate_score,
    estimate_entropy,
    strength_bar,
    generate_password,
    save_history,
    crack_time
)


def main():

    print("=" * 45)
    print("PASSWORD STRENGTH ANALYZER")
    print("=" * 45)

    print("\n 1. Analyze Password")
    print("2. Generate Strong Password")
    print("3. Exit")

    choice = input("\nChoose an option (1-3): ")

    # choice is 2
    if choice == "2":

        length = int(input("\nEnter password length: "))

        new_password = generate_password(length)

        print("\nGenerated Password:")
        print(new_password)

        return

    # choice is 3

    elif choice == "3":

        print("\nThank you for using Password Strength Analyzer!")
        return

    # choice is 1
    elif choice == "1":

        attempts = 0
        max_attempts = 3

        while attempts < max_attempts:

            password = input("\nEnter your password: ")

            length = check_length(password)

            if length:
                print("\n Password length is good.")
                break

            attempts += 1
            remaining = max_attempts - attempts

            if remaining > 0:
                print("\n Password must be at least 8 characters long.")
                print(f" You have {remaining} attempt(s) left.")

            else:
                print("\n Maximum attempts reached.")
                print("Access Denied!")
                return

        # Password Analysis

        upper = check_uppercase(password)
        lower = check_lowercase(password)
        number = check_numbers(password)
        special = check_special_characters(password)
        common = check_common_password(password)
        score = calculate_score(
            length,
            upper,
            lower,
            number,
            special
        )
        save_history(password, score)
        entropy = estimate_entropy(score)
        bar = strength_bar(score)
        time = crack_time(score)
        

        print(f"Estimated Crack Time : {time}")
        print("\n")
        print("=" * 45)
        print("PASSWORD REPORT")
        print("=" * 45)

        if upper:
            print("Uppercase Letter      : Present")
        else:
            print("Uppercase Letter      : Missing")

        if lower:
            print("Lowercase Letter      : Present")
        else:
            print("Lowercase Letter      : Missing")

        if number:
            print("Numbers               : Present")
        else:
            print("Numbers               : Missing")

        if special:
            print("Special Characters    : Present")
        else:
            print("Special Characters    : Missing")

        if common:
            print("Common Password       : Yes")
        else:
            print("Common Password       : No")

        print("\n------------------------------")
        print(f"Password Score : {score}/5")
        print("\nPassword Strength")
        print(bar)
        print(f"Estimated Security : {entropy}")
        if score == 5:
            print("Strength :  Very Strong")
        elif score == 4:
            print("Strength :  Strong")
        elif score == 3:
            print("Strength :  Medium")
        elif score == 2:
            print("Strength :  Weak")
        else:
            print("Strength :  Very Weak")

        print("\nSuggestions:")

        if not upper:
            print("- Add at least one uppercase letter.")

        if not lower:
            print("- Add at least one lowercase letter")

        if not number:
            print("- Add at least one number")

        if not special:
            print("- Add at least one special character")

        if common:
            print("- Avoid using common passwords")

        if score == 5:
            print("Excellent! Your password follows all basic security rules")

    else:
        print("\nInvalid choice. Please run the program again")


if __name__ == "__main__":
    main()