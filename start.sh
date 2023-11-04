#!/bin/bash
source venv/bin/activate

# Set environment variables if needed
export FLASK_APP=app.py
export FLASK_ENV=production

# Start the Flask app
flask run --host 0.0.0.0 --port $PORT
