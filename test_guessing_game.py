import pytest
from guessing_game import number_guessing_game
from io import StringIO
import sys

def test_correct_guess(monkeypatch):
    # Simulate user input
    monkeypatch.setattr('sys.stdin', StringIO("23\n"))
    # Redirect stdout to capture the output
    output = StringIO()
    monkeypatch.setattr('sys.stdout', output)
    number_guessing_game()
    # Check if the correct message is in the output
    assert "Congratulations! You guessed the number!" in output.getvalue()

def test_incorrect_guesses(monkeypatch):
    # Simulate user input
    monkeypatch.setattr('sys.stdin', StringIO("1\n2\n3\n4\n5\n23\n"))
    # Redirect stdout to capture the output
    output = StringIO()
    monkeypatch.setattr('sys.stdout', output)
    number_guessing_game()
    # Check if the final correct guess message is in the output
    assert "Congratulations! You guessed the number!" in output.getvalue()

def test_guess_too_low(monkeypatch):
    # Simulate user input
    monkeypatch.setattr('sys.stdin', StringIO("1\n23\n"))
    # Redirect stdout to capture the output
    output = StringIO()
    monkeypatch.setattr('sys.stdout', output)
    number_guessing_game()
    # Check if the "too low" message is in the output
    assert "Guess higher!" in output.getvalue()

def test_guess_too_high(monkeypatch):
    # Simulate user input
    monkeypatch.setattr('sys.stdin', StringIO("25\n23\n"))
    # Redirect stdout to capture the output
    output = StringIO()
    monkeypatch.setattr('sys.stdout', output)
    number_guessing_game()
    # Check if the "too high" message is in the output
    assert "Guess lower!" in output.getvalue()

def test_invalid_input(monkeypatch):
    # Simulate user input
    monkeypatch.setattr('sys.stdin', StringIO("abc\n23\n"))
    # Redirect stdout to capture the output
    output = StringIO()
    monkeypatch.setattr('sys.stdout', output)
    number_guessing_game()
    # Check if the invalid input message is in the output
    assert "Invalid input. Please enter a number." in output.getvalue()
