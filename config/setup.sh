#!/bin/bash

# YouGen AI YouTube Content Generator - Automated Setup Script
# For Envato Buyers - One-Click Installation

set -e  # Exit on any error

echo "🎬 YouGen AI YouTube Content Generator"
echo "=========================================="
echo "🚀 Automated Setup for Envato Buyers"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if running on Windows
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    print_error "This script is for macOS/Linux. For Windows, please follow the manual installation guide in INSTALLATION.md"
    exit 1
fi

print_status "Starting automated setup..."

# Step 1: Check Python installation
print_status "Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    print_success "Python $PYTHON_VERSION found"
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version | cut -d' ' -f2)
    print_success "Python $PYTHON_VERSION found"
    PYTHON_CMD="python"
else
    print_error "Python not found. Please install Python 3.8+ from https://python.org"
    exit 1
fi

# Check Python version
PYTHON_MAJOR=$($PYTHON_CMD -c "import sys; print(sys.version_info.major)")
PYTHON_MINOR=$($PYTHON_CMD -c "import sys; print(sys.version_info.minor)")

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 8 ]); then
    print_error "Python 3.8+ required. Current version: $PYTHON_VERSION"
    exit 1
fi

# Step 2: Create virtual environment
print_status "Creating Python virtual environment..."
if [ -d "venv" ]; then
    print_warning "Virtual environment already exists. Removing old one..."
    rm -rf venv
fi

$PYTHON_CMD -m venv venv
print_success "Virtual environment created"

# Step 3: Activate virtual environment
print_status "Activating virtual environment..."
source venv/bin/activate
print_success "Virtual environment activated"

# Step 4: Upgrade pip
print_status "Upgrading pip..."
pip install --upgrade pip
print_success "Pip upgraded"

# Step 5: Install Python dependencies
print_status "Installing Python dependencies..."
if [ -f "requirements.txt" ]; then
pip install -r requirements.txt
    print_success "Python dependencies installed"
else
    print_error "requirements.txt not found"
    exit 1
fi

# Step 6: Check if Ollama is installed
print_status "Checking Ollama installation..."
if command -v ollama &> /dev/null; then
    print_success "Ollama found"
else
    print_status "Installing Ollama..."
    curl -fsSL https://ollama.ai/install.sh | sh
    print_success "Ollama installed"
fi

# Step 7: Start Ollama service
print_status "Starting Ollama service..."
if ! pgrep -x "ollama" > /dev/null; then
    ollama serve &
    OLLAMA_PID=$!
    sleep 5  # Wait for Ollama to start
    print_success "Ollama service started"
else
    print_success "Ollama service already running"
fi

# Step 8: Download AI model
print_status "Downloading AI model (this may take a few minutes)..."
if ollama list | grep -q "gemma:2b"; then
    print_success "AI model already downloaded"
else
    ollama pull gemma:2b
    print_success "AI model downloaded"
fi

# Step 9: Create .env file
print_status "Creating configuration file..."
if [ ! -f ".env" ]; then
    cat > .env << EOF
SECRET_KEY=$(python -c "import secrets; print(secrets.token_hex(32))")
FLASK_DEBUG=True
PORT=5000
EOF
    print_success "Configuration file created"
else
    print_success "Configuration file already exists"
fi

# Step 10: Test the application
print_status "Testing application..."
if curl -s http://localhost:11434/api/tags > /dev/null; then
    print_success "Ollama API is responding"
else
    print_warning "Ollama API not responding. Please restart Ollama manually: ollama serve"
fi

# Step 11: Create start script
print_status "Creating start script..."
cat > start.sh << 'EOF'
#!/bin/bash
echo "🎬 Starting YouGen AI YouTube Content Generator..."
echo ""

# Activate virtual environment
source venv/bin/activate

# Start the application
python app.py
EOF

chmod +x start.sh
print_success "Start script created"

# Step 12: Create stop script
print_status "Creating stop script..."
cat > stop.sh << 'EOF'
#!/bin/bash
echo "🛑 Stopping YouGen AI YouTube Content Generator..."

# Kill Python processes
pkill -f "python.*app.py" || true

# Kill Ollama process
pkill -f "ollama serve" || true

echo "✅ Application stopped"
EOF

chmod +x stop.sh
print_success "Stop script created"

# Final success message
echo ""
echo "🎉 SETUP COMPLETE!"
echo "=================="
echo ""
echo "✅ Your AI YouTube Content Generator is ready to use!"
echo ""
echo "🚀 To start the application:"
echo "   ./start.sh"
echo ""
echo "🌐 Open your browser and go to:"
echo "   http://localhost:5000"
echo ""
echo "🛑 To stop the application:"
echo "   ./stop.sh"
echo ""
echo "📚 For detailed instructions, see:"
echo "   - INSTALLATION.md (Quick guide)"
echo "   - README.md (Complete documentation)"
echo ""
echo "🎬 Start creating viral YouTube content now!"
echo ""
echo "Need help? Contact: support@YouGen.com"
echo ""

# Optional: Start the application
read -p "Would you like to start the application now? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🚀 Starting application..."
    ./start.sh
fi
