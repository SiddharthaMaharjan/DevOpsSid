# Environment setup
VENV_NAME := venv
PYTHON := python

# OS-specific paths
ifeq ($(OS),Windows_NT)
    PIP := $(VENV_NAME)/Scripts/pip
    PYTEST := $(VENV_NAME)/Scripts/pytest
else
    PIP := $(VENV_NAME)/bin/pip
    PYTEST := $(VENV_NAME)/bin/pytest
endif

# Build targets
all: install test package

install:
	echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV_NAME)
	echo "Installing dependencies..."
	$(PIP) install -r requirements.txt

test:
	echo "Running unit tests..."
	$(PYTEST) -s test_guessing_game.py

package:
	echo "Packaging application..."
	$(PIP) freeze > requirements.txt
	echo "Build complete!"

clean:
	echo "Cleaning up..."
	-rm -rf $(VENV_NAME)
	echo "Clean complete!"
