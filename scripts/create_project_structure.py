"""
Lab-VC — Project Structure Initialization Script

This script creates the standard directory structure for the
Lab-VC (Vision Computing Laboratory) project.

IMPORTANT:
- This script must be executed from the ROOT of the repository.
- It does NOT create a new 'lab-vc' folder.
- All directories are created relative to the current working directory.
"""

import os

# List of directories to be created in the project root
DIRECTORIES = [
    "data/raw",
    "data/processed",
    "docs",
    "notebooks/phase_0",
    "notebooks/phase_1",
    "notebooks/phase_2",
    "src/data",
    "src/models",
    "src/utils"
]

# List of files to be created in the project root
FILES = [
    "requirements.txt"
]

def create_directories():
    """
    Create project directories if they do not already exist.
    """
    for directory in DIRECTORIES:
        os.makedirs(directory, exist_ok=True)

def create_files():
    """
    Create empty files if they do not already exist.
    """
    for file in FILES:
        if not os.path.exists(file):
            with open(file, "w") as f:
                pass

if __name__ == "__main__":
    create_directories()
    create_files()
    print("Lab-VC project structure created successfully.")
