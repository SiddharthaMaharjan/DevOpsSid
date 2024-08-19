import pytest
import random
from guessing_game import number_guessing_game
from io import StringIO  # To simulate input

def test_correct_guess(monkeypatch):
    # Mock the random number to a known value, e.g., 23
    monkeypatch.setattr(random, 'randint', lambda a, b: 23)
    # Simulate the sequence of inputs that ends with the correct guess
    monkeypatch.setattr('sys.stdin', StringIO("10\n15\n20\n23\n"))
    number_guessing_game()  # Call without any arguments

def test_incorrect_guesses(monkeypatch):
    # Mock the random number to a known value, e.g., 23
    monkeypatch.setattr(random, 'randint', lambda a, b: 23)
    # Simulate enough incorrect guesses to exhaust all attempts
    monkeypatch.setattr('sys.stdin', StringIO("1\n2\n3\n4\n5\n30\n35\n40\n45\n50\n"))
    number_guessing_game()  # Call without any arguments

def test_guess_too_low(monkeypatch):
    # Mock the random number to a known value, e.g., 23
    monkeypatch.setattr(random, 'randint', lambda a, b: 23)
    # Simulate a guess that is too low
    monkeypatch.setattr('sys.stdin', StringIO("1\n"))
    number_guessing_game()  # Call without any arguments

def test_guess_too_high(monkeypatch):
    # Mock the random number to a known value, e.g., 23
    monkeypatch.setattr(random, 'randint', lambda a, b: 23)
    # Simulate a guess that is too high
    monkeypatch.setattr('sys.stdin', StringIO("25\n"))
    number_guessing_game()  # Call without any arguments

def test_invalid_input(monkeypatch):
    # Mock the random number to a known value, e.g., 23
    monkeypatch.setattr(random, 'randint', lambda a, b: 23)
    # Simulate invalid input
    monkeypatch.setattr('sys.stdin', StringIO("abc\n"))
    number_guessing_game()  # Call without any arguments
