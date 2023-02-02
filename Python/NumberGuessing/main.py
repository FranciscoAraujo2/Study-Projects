import random

def main():
    # print prompt to user
    print("Guess the number between 1 and 100")
    
    # generate a random number between 1 and 100
    number = random.randint(1,100)
    guess = None
    
    # loop until user correctly guesses the number
    while guess != number:
        guess = int(input("Enter your guess: "))
        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
    print(f"You got it!. \nNumber: {number}")

# run main function if the script is run directly
if __name__ == '__main__':
    main()
