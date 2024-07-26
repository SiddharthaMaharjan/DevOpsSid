import random

def number_guessing_game():

    secret_number = random.randint(1, 30)
    attempts = 5


    print("I'm thinking of a number between 1 and 20.")

    while True:
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Please enter a number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job! You guessed my number in {attempts} attempts!")
            break

if __name__ == "__main__":
    number_guessing_game()