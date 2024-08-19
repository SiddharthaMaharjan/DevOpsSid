import random

def number_guessing_game():
    secret_number = random.randint(1, 20)  # Match the range to the prompt
    attempts = 0  # Start attempts from 0

    print("I'm thinking of a number between 1 and 20.")

    while True:
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Please enter a number.")
            continue

        attempts += 1  # Increment the number of attempts only after a valid guess

        if guess < secret_number:
            print("Oops! Aim higher.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed my number in {attempts} attempts!")
            break

if __name__ == "__main__":
    number_guessing_game()

