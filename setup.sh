#!/bin/bash

# Setup script for AskExpertProjectModelLlama2

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create required directories
mkdir -p data
mkdir -p logs
mkdir -p models

echo "Setup complete!"