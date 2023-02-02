import random

def main():
    print("Guess the number between 1 and 100")
    number = random.randint(1,100)
    guess = None
    while guess != number:
        guess = int(input("Enter your guess: "))
        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
    print(f"You got it!. \nNumber: {number}")

if __name__ == '__main__':
    main()
