import random

def number_guessing_game():
    secret_number = random.randint(1, 20)  # Correct the range to 1-20
    attempts = 5

    print("I'm thinking of a number between 1 and 20.")
    print(f"You have {attempts} attempts to guess it.")

    while attempts > 0:
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts -= 1  # Decrement attempts for each guess

        if guess < secret_number:
            print("Oops! Aim higher.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed my number in {5 - attempts} attempts!")
            break
    else:
        print(f"Sorry, you're out of attempts. The number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
