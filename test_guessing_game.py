import pytest
from guessing_game import number_guessing_game
from io import StringIO

def test_correct_guess(monkeypatch):
    # Simulate entering the correct guess
    monkeypatch.setattr('builtins.input', lambda _: "23")
    with pytest.raises(SystemExit):
        number_guessing_game()

def test_incorrect_guesses(monkeypatch):
    # Simulate making several incorrect guesses followed by the correct guess
    input_values = iter(["1", "2", "3", "4", "5", "23"])
    monkeypatch.setattr('builtins.input', lambda _: next(input_values))
    with pytest.raises(SystemExit):
        number_guessing_game()

def test_guess_too_low(monkeypatch):
    # Simulate entering a guess that is too low
    monkeypatch.setattr('builtins.input', lambda _: "1")
    with pytest.raises(SystemExit):
        number_guessing_game()

def test_guess_too_high(monkeypatch):
    # Simulate entering a guess that is too high
    monkeypatch.setattr('builtins.input', lambda _: "30")
    with pytest.raises(SystemExit):
        number_guessing_game()

def test_invalid_input(monkeypatch):
    # Simulate entering an invalid input followed by a correct guess
    input_values = iter(["abc", "23"])
    monkeypatch.setattr('builtins.input', lambda _: next(input_values))
    with pytest.raises(SystemExit):
        number_guessing_game()
