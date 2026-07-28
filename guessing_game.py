import random

print("===== Number Guessing Game =====")
print("Welcome! Try to guess the secret number.\n")

# Choose difficulty
print("Select difficulty level:")
print("1. Easy (1 - 10, 5 attempts)")
print("2. Medium (1 - 50, 7 attempts)")
print("3. Hard (1 - 100, 10 attempts)")

difficulty = input("Enter your choice (1, 2 or 3): ")

if difficulty == "1":
    secret_number = random.randint(1, 10)
    max_attempts = 5
    range_text = "1 and 10"
elif difficulty == "2":
    secret_number = random.randint(1, 50)
    max_attempts = 7
    range_text = "1 and 50"
else:
    secret_number = random.randint(1, 100)
    max_attempts = 10
    range_text = "1 and 100"

print(f"\nI'm thinking of a number between {range_text}.")
print(f"You have {max_attempts} attempts.\n")

attempts = 0
won = False

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.\n")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"\nCongratulations! You guessed the number in {attempts} attempts.")
        won = True
        break

    remaining = max_attempts - attempts
    if remaining > 0:
        print(f"Attempts remaining: {remaining}\n")

if not won:
    print(f"\nGame Over! The secret number was {secret_number}.")

print("\nThanks for playing!")