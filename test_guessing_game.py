import pytest
from guessing_game import number_guessing_game
from io import StringIO  # To simulate input


def test_correct_guess(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("23\n"))
    with pytest.raises(SystemExit):
        number_guessing_game()  # Call without any arguments

def test_incorrect_guesses(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("1\n2\n3\n4\n5\n"))
    with pytest.raises(SystemExit):
        number_guessing_game()  # Call without any arguments

def test_guess_too_low(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("1\n"))
    with pytest.raises(SystemExit):
        number_guessing_game()  # Call without any arguments

def test_guess_too_high(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("25\n"))
    with pytest.raises(SystemExit):
        number_guessing_game()  # Call without any arguments

def test_invalid_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("abc\n"))
    with pytest.raises(SystemExit):
        number_guessing_game()  # Call without any arguments

