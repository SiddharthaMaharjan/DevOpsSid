import pytest
from guessing_game import number_guessing_game
from io import StringIO

def test_correct_guess(monkeypatch):
    # Simulate entering the correct guess
    monkeypatch.setattr('sys.stdin', StringIO("23\n"))
    with pytest.raises(SystemExit):
        number_guessing_game()

def test_incorrect_guesses(monkeypatch):
    # Simulate making several incorrect guesses
    monkeypatch.setattr('sys.stdin', StringIO("1\n2\n3\n4\n5\n23\n"))
    with pytest.raises(SystemExit):
        number_guessing_game()

def test_guess_too_low(monkeypatch):
    # Simulate entering a guess that is too low
    monkeypatch.setattr('sys.stdin', StringIO("1\n"))
    with pytest.raises(SystemExit):
        number_guessing_game()

def test_guess_too_high(monkeypatch):
    # Simulate entering a guess that is too high
    monkeypatch.setattr('sys.stdin', StringIO("25\n"))
    with pytest.raises(SystemExit):
        number_guessing_game()

def test_invalid_input(monkeypatch):
    # Simulate entering an invalid input
    monkeypatch.setattr('sys.stdin', StringIO("abc\n23\n"))
    with pytest.raises(SystemExit):
        number_guessing_game()
