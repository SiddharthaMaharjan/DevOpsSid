# Environment Setup
VENV_NAME := venv
PYTHON := python

# OS Detection (adjust paths if needed)
ifeq ($(OS),Windows_NT)
    VENV_BIN := $(VENV_NAME)/Scripts
else
    VENV_BIN := $(VENV_NAME)/bin
endif

# Build Targets
all: install test

install:
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV_NAME)
	@echo "Installing dependencies..."
	$(VENV_BIN)/pip install -r requirements.txt

test:
	@echo "Running unit tests..."
	$(VENV_BIN)/pytest 

package:  
	@echo "Packaging application..."
	# Your packaging commands here (e.g., using setuptools or poetry)

clean:
	@echo "Cleaning up..."
	rm -rf $(VENV_NAME)  # Adjust for Windows if needed (e.g., 'rmdir /s /q venv')