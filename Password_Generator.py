import random
import string                                                        

def generate_password(length, use_digits=True, use_symbols=True):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Base character set
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("=== Password Generator ===")
    try:
        # Get password length
        length = int(input("Enter password length: "))

        # Get user preferences
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        # Generate password
        password = generate_password(length, use_digits, use_symbols)
        print("Generated Password:", password)

    except ValueError:
        print("Please enter a valid number.")


# Run the main function
if __name__ == "__main__":
    main()
