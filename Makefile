# Environment setup
VENV_NAME := venv
PYTHON := python

# Check if OS is Windows or UNIX-like
ifeq ($(OS),Windows_NT)
    PIP := $(VENV_NAME)/Scripts/pip
    PYTHON_VENV := $(VENV_NAME)/Scripts/python
else
    PIP := $(VENV_NAME)/bin/pip
    PYTHON_VENV := $(VENV_NAME)/bin/python
endif

# Build targets
all: install test package

install:
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV_NAME)
	@echo "Installing dependencies..."
	$(PIP) install -r requirements.txt

test:
	@echo "Running unit tests..."
	$(PYTHON_VENV) -m pytest -s test_guessing_game.py

package:
	@echo "Packaging application..."
	$(PIP) freeze > requirements.txt
	@echo "Build complete!"

clean:
	@echo "Cleaning up..."
	rm -rf $(VENV_NAME)
