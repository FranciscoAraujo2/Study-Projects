import random
import string

def generate_password():
    # Initialize the set of characters to use in the password
    characters = ""

    # Ask the user which characters to include in the password
    include_letters = input("Include letters (y/n)? ")
    if include_letters.lower() == "y":
        characters += string.ascii_letters

    include_digits = input("Include digits (y/n)? ")
    if include_digits.lower() == "y":
        characters += string.digits

    include_punctuation = input("Include punctuation (y/n)? ")
    if include_punctuation.lower() == "y":
        characters += string.punctuation

    # Ask the user for the password length
    length = int(input("Enter the desired length of the password: "))

    # Initialize an empty string to store the password
    password = ""

    # Generate the password
    for i in range(length):
        # Choose a random character from the set of characters
        index = int(random.random() * len(characters))
        password += characters[index]

    return password

# Call the password generator function
password = generate_password()
print("Password:", password)
