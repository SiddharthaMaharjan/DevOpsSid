import pytest
from guessing_game import number_guessing_game
from io import StringIO  # To simulate input

def test_correct_guess(monkeypatch):
    # Simulate a sequence of inputs that ends with the correct guess
    monkeypatch.setattr('sys.stdin', StringIO("10\n15\n20\n23\n"))
    number_guessing_game()  # Call without any arguments

def test_incorrect_guesses(monkeypatch):
    # Simulate incorrect guesses until the game ends
    monkeypatch.setattr('sys.stdin', StringIO("1\n2\n3\n4\n5\n"))
    number_guessing_game()  # Call without any arguments

def test_guess_too_low(monkeypatch):
    # Simulate a guess that is too low
    monkeypatch.setattr('sys.stdin', StringIO("1\n"))
    number_guessing_game()  # Call without any arguments

def test_guess_too_high(monkeypatch):
    # Simulate a guess that is too high
    monkeypatch.setattr('sys.stdin', StringIO("25\n"))
    number_guessing_game()  # Call without any arguments

def test_invalid_input(monkeypatch):
    # Simulate invalid input
    monkeypatch.setattr('sys.stdin', StringIO("abc\n"))
    number_guessing_game()  # Call without any arguments
