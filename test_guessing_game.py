import pytest
from guessing_game import number_guessing_game
from io import StringIO

def test_correct_guess(monkeypatch):
    # Simulate entering the correct guess
    monkeypatch.setattr('builtins.input', lambda _: "23")
    with pytest.raises(SystemExit):
        number_guessing_game()

# Comment out other tests and run this one first
# Add them back one by one to see where the issue arises

