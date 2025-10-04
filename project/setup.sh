#!/bin/bash

# setup.sh - Setup script for UWaterloo Prof Finder
# This script creates a virtual environment, installs dependencies, and runs the app

set -e  # Exit on error

echo "Setting up UWaterloo Prof Finder..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Run the Streamlit app
echo "Starting Streamlit app..."
streamlit run frontend.py