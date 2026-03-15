# Dice rolling simulator

import random

while True:
    input("Press Enter to roll the dice...")
    
    number = random.randint(1, 6)
    print("You rolled:", number)
    
    again = input("Roll again? (yes/no): ").lower()
    
    if again != "yes":
        break
