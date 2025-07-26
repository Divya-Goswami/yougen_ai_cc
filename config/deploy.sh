#!/bin/bash

echo "🚀 AI YouTube Generator - Marketplace Deployment Script"
echo "=================================================="

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📁 Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit - AI YouTube Generator"
fi

# Check if requirements are installed
echo "📦 Checking dependencies..."
if ! python -c "import flask, ollama, gunicorn, dotenv" 2>/dev/null; then
    echo "⚠️  Installing missing dependencies..."
    pip install -r requirements.txt
fi

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "🔧 Creating .env file..."
    cat > .env << EOF
SECRET_KEY=your-secret-key-change-in-production
FLASK_DEBUG=True
PORT=5000
EOF
    echo "✅ Created .env file (update SECRET_KEY for production)"
fi

# Check if Ollama is running
echo "🤖 Checking Ollama status..."
if ! curl -s http://localhost:11434/api/tags > /dev/null; then
    echo "⚠️  Ollama is not running. Please start it with: ollama serve"
    echo "   Then pull the model with: ollama pull mistral"
else
    echo "✅ Ollama is running"
fi

echo ""
echo "🎯 Deployment Options:"
echo "1. Heroku"
echo "2. Railway"
echo "3. Render"
echo "4. Local Development"
echo ""

read -p "Choose deployment option (1-4): " choice

case $choice in
    1)
        echo "🚀 Deploying to Heroku..."
        if ! command -v heroku &> /dev/null; then
            echo "❌ Heroku CLI not found. Install from: https://devcenter.heroku.com/articles/heroku-cli"
            exit 1
        fi
        
        read -p "Enter Heroku app name: " app_name
        heroku create $app_name
        heroku config:set SECRET_KEY=$(python -c "import secrets; print(secrets.token_hex(32))")
        heroku config:set FLASK_DEBUG=False
        git add .
        git commit -m "Deploy to Heroku"
        git push heroku main
        echo "✅ Deployed to: https://$app_name.herokuapp.com"
        ;;
    2)
        echo "🚂 Deploying to Railway..."
        echo "1. Go to https://railway.app"
        echo "2. Connect your GitHub repository"
        echo "3. Set environment variables:"
        echo "   - SECRET_KEY: $(python -c "import secrets; print(secrets.token_hex(32))")"
        echo "   - FLASK_DEBUG: False"
        echo "4. Deploy automatically"
        ;;
    3)
        echo "🎨 Deploying to Render..."
        echo "1. Go to https://render.com"
        echo "2. Create new Web Service"
        echo "3. Connect your GitHub repository"
        echo "4. Set build command: pip install -r requirements.txt"
        echo "5. Set start command: gunicorn app:app"
        echo "6. Set environment variables:"
        echo "   - SECRET_KEY: $(python -c "import secrets; print(secrets.token_hex(32))")"
        echo "   - FLASK_DEBUG: False"
        ;;
    4)
        echo "💻 Starting local development server..."
        python app.py
        ;;
    *)
        echo "❌ Invalid option"
        exit 1
        ;;
esac

echo ""
echo "🎉 Deployment complete!"
echo "📚 Check README.md for detailed instructions"
echo "🔗 Health check: curl https://your-app-url/health" 