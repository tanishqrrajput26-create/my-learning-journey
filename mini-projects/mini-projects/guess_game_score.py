# Number guessing game with attempts

import random

number = random.randint(1, 20)
attempts = 0

while True:
    guess = int(input("Guess the number (1-20): "))
    attempts += 1

    if guess == number:
        print("Correct! Attempts:", attempts)
        break
    elif guess < number:
        print("Too low")
    else:
        print("Too high")
