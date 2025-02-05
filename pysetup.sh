#!/bin/bash

# Setting up a Python environment and running the script on Mac

# Step 1: Install Python if not installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found. Please install it from https://www.python.org/downloads/"
    exit
fi

echo "Python3 is installed. Proceeding with setup..."

# Step 2: Create a Virtual Environment
if [ ! -d "env" ]; then
    python3 -m venv env
    echo "Virtual environment created."
else
    echo "Virtual environment already exists."
fi

# Step 3: Activate the Virtual Environment
source env/bin/activate

echo "Virtual environment activated."

# Step 4: Install Dependencies
pip install --upgrade pip
pip install requests beautifulsoup4

echo "Dependencies installed."

# Step 5: Run the Python Script
echo "Running the script..."
python3 your_script.py  # Replace with actual script name

echo "Script execution completed."

deactivate

echo "Virtual environment deactivated."