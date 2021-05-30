#!/bin/bash

# Download selected model
python src/startup.py
# Start web server
gunicorn --bind 0.0.0.0:8000 --pythonpath src server:app