import random
import math

# Take lower and upper bound from user
a = int(input("Enter Lower Bound: "))
b = int(input("Enter Upper Bound: "))

# Ensure correct range
if a > b:
    print("Invalid bounds. Lower bound must be less than or equal to upper bound.")
    exit()

range_size = b - a + 1
random_number = random.randint(a, b)

# Calculate max number of guesses using binary search principle
total_guess = math.ceil(math.log2(range_size))

print(f"\nYou have {total_guess} attempts to guess the number between {a} and {b}.")

while total_guess > 0:
    try:
        guessed_number = int(input("Guess a number: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        continue

    if guessed_number < a or guessed_number > b:
        print("Out of range! Please guess within the specified bounds.")
        continue

    if guessed_number == random_number:
        print("🎉 Congratulations! You guessed the correct number!")
        break
    elif guessed_number > random_number:
        total_guess -= 1
        print(f"📉 Too high! Remaining guesses: {total_guess}")
    else:
        total_guess -= 1
        print(f"📈 Too low! Remaining guesses: {total_guess}")

if total_guess == 0:
    print(f"❌ You lost! The correct number was {random_number}.")
