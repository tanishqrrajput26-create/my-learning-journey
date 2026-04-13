# Simple number guessing game

secret_number = 7

guess = int(input("Guess the number (1-10): "))

if guess == secret_number:

    print("Correct guess!")
else:
    print("Wrong guess. Try again.")