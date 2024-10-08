import pytest
import random
from guessing_game import number_guessing_game
from io import StringIO  # To simulate input

def test_correct_guess(monkeypatch):
    monkeypatch.setattr(random, 'randint', lambda a, b: 23)
    monkeypatch.setattr('sys.stdin', StringIO("10\n15\n20\n23\n"))
    number_guessing_game()  # Call without any arguments

def test_incorrect_guesses(monkeypatch):
    monkeypatch.setattr(random, 'randint', lambda a, b: 23)
    monkeypatch.setattr('sys.stdin', StringIO("1\n2\n3\n4\n5\n30\n35\n40\n45\n50\n55\n60\n"))
    number_guessing_game()  # Call without any arguments

def test_guess_too_low(monkeypatch):
    monkeypatch.setattr(random, 'randint', lambda a, b: 23)
    monkeypatch.setattr('sys.stdin', StringIO("1\n2\n3\n4\n5\n"))
    number_guessing_game()  # Call without any arguments

def test_guess_too_high(monkeypatch):
    monkeypatch.setattr(random, 'randint', lambda a, b: 23)
    monkeypatch.setattr('sys.stdin', StringIO("25\n30\n35\n40\n45\n"))
    number_guessing_game()  # Call without any arguments

def test_invalid_input(monkeypatch):
    monkeypatch.setattr(random, 'randint', lambda a, b: 23)
    # Provide invalid input followed by valid attempts
    monkeypatch.setattr('sys.stdin', StringIO("abc\n10\n20\n23\n"))
    number_guessing_game()  # Call without any arguments
