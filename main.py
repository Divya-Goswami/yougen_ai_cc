#!/usr/bin/env python3
"""
YouGen AI - YouTube Content Generator
Main Application Entry Point

This is the main entry point for the YouGen AI application.
It imports the Flask app from the organized source structure and runs it.
"""

import os
import sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from controllers.app import app

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    # Run the Flask application
    app.run(
        host='0.0.0.0',
        port=port,
        debug=os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    ) 