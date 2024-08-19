Makefile
# Environment setup
VENV_NAME := venv
PYTHON := python

# Build targets
all: install test package

install:
    @echo "Creating virtual environment..."
    $(PYTHON) -m venv $(VENV_NAME)
    @echo "Installing dependencies..."
    $(VENV_NAME)/Scripts/pip install -r requirements.txt

test:
    @echo "Running unit tests..."
    $(VENV_NAME)/Scripts/pytest -s test_guessing_game.py

package:
    @echo "Packaging application..."
    $(VENV_NAME)/Scripts/pip freeze > requirements.txt
    @echo "Build complete!"
