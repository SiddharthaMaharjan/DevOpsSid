import pytest
from guessing_game import number_guessing_game
from io import StringIO
import sys

def mock_input(prompt):
    return StringIO("25\n").readline()

def test_correct_guess(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("25\n"))
    with pytest.raises(SystemExit):
        number_guessing_game()

def test_incorrect_guesses(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("1\n2\n3\n4\n5\n25\n"))
    with pytest.raises(SystemExit):
        number_guessing_game()

def test_guess_too_low(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("1\n"))
    with pytest.raises(SystemExit):
        number_guessing_game()

def test_guess_too_high(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("31\n"))
    with pytest.raises(SystemExit):
        number_guessing_game()

def test_invalid_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("abc\n"))
    with pytest.raises(SystemExit):
        number_guessing_game()
