import random

def number_guessing_game():
    secret_number = random.randint(1, 30)
    attempts = 5

    print("I'm thinking of a number between 1 and 20.")
    for _ in range(attempts):  # Limit the number of attempts
        try:
            guess = int(input("Take  guess: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if guess < secret_number:
            print("Oops! Aim higher.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed my number in {attempts} attempts!")
            return
    print("Sorry, you've run out of attempts!")
