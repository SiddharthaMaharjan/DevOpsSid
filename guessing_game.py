import random

def number_guessing_game(secret_number=None, guess=None):
    if secret_number is None:
        secret_number = random.randint(1, 20)
    
    attempts = 0
    
    while True:
        if guess is not None:
            try:
                guess = int(guess)
            except ValueError:
                return "Please enter a number."
                
            attempts += 1

            if guess < secret_number:
                return "Oops! Aim higher."
            elif guess > secret_number:
                return "Your guess is too high."
            else:
                return f"Congratulations! You guessed my number in {attempts} attempts!"
        else:
            return "No guess provided."

if __name__ == "__main__":
    number_guessing_game()
