import pytest
from guessing_game import number_guessing_game

def test_correct_guess(monkeypatch):
    input_values = ["23"]
    def mock_input(prompt):
        return input_values.pop(0) if input_values else '23'
    monkeypatch.setattr('builtins.input', mock_input)
    with pytest.raises(SystemExit):
        number_guessing_game()

def test_incorrect_guesses(monkeypatch):
    input_values = ["1", "2", "3", "4", "5", "23"]
    def mock_input(prompt):
        return input_values.pop(0) if input_values else '23'
    monkeypatch.setattr('builtins.input', mock_input)
    with pytest.raises(SystemExit):
        number_guessing_game()

def test_guess_too_low(monkeypatch):
    input_values = ["1"]
    def mock_input(prompt):
        return input_values.pop(0) if input_values else '1'
    monkeypatch.setattr('builtins.input', mock_input)
    with pytest.raises(SystemExit):
        number_guessing_game()

def test_guess_too_high(monkeypatch):
    input_values = ["25"]
    def mock_input(prompt):
        return input_values.pop(0) if input_values else '25'
    monkeypatch.setattr('builtins.input', mock_input)
    with pytest.raises(SystemExit):
        number_guessing_game()

def test_invalid_input(monkeypatch):
    input_values = ["abc"]
    def mock_input(prompt):
        return input_values.pop(0) if input_values else 'abc'
    monkeypatch.setattr('builtins.input', mock_input)
    with pytest.raises(SystemExit):
        number_guessing_game()

