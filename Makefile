VENV_NAME := venv
PYTHON := python
PIP := $(VENV_NAME)/Scripts/pip
PYTEST := $(VENV_NAME)/Scripts/pytest

# Build targets
all: install test package

install:
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV_NAME)
	@echo "Installing dependencies..."
	$(PIP) install -r requirements.txt

test:
	@echo "Running unit tests..."
	$(PYTEST) -s test_guessing_game.py

package:
	@echo "Packaging application..."
	$(PIP) freeze > requirements.txt