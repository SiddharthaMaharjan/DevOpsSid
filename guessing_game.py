import random
import sys

def number_guessing_game():
    secret_number = random.randint(1, 30)
    attempts = 0

    print("I'm thinking of a number between 1 and 30.")

    while attempts < 5:
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Oops! Aim higher.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed my number in {attempts} attempts!")
            sys.exit(0)

    print(f"Sorry, you've used all attempts. The number was {secret_number}.")
    sys.exit(1)

if __name__ == "__main__":
    number_guessing_game()
