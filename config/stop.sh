#!/bin/bash
echo "🛑 Stopping YouGen AI YouTube Content Generator..."

# Kill Python processes
pkill -f "python.*app.py" || true

# Kill Ollama process
pkill -f "ollama serve" || true

echo "✅ Application stopped"
