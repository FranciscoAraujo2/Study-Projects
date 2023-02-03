# Define global variables for the username and password
username = ""
password = ""

def register_account():
    # Access the global variables for username and password
    global username
    global password

    username = input("Enter a username: ")
    password = input("Enter a password: ")
    print("\nAccount registered successfully \n")

def login():
    # Access the global variables for username and password
    global username
    global password

    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")

    # Check if the entered username and password match the predefined values
    if entered_username == username and entered_password == password:
        print("\nLogin successful\n")
    else:
        print("Login failed")

if __name__ == "__main__":
    register_account()
    login()
