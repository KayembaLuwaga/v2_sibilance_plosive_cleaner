#!/bin/bash
set -e

# Create and activate the virtual environment
python -m venv venv
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate
