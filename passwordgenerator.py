import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    """Generate a random password."""
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    # Create a pool of characters to choose from
    characters = string.ascii_lowercase  # Start with lowercase letters
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    length = int(input("Enter the desired password length (default is 12): ") or 12)
    use_uppercase = input("Include uppercase letters? (y/n, default is y): ").lower() != 'n'
    use_digits = input("Include digits? (y/n, default is y): ").lower() != 'n'
    use_special = input("Include special characters? (y/n, default is y): ").lower() != 'n'

    password = generate_password(length, use_uppercase, use_digits, use_special)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
