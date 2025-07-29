# 🚀 Quick Installation Guide

## For Envato Buyers - Get Started in 5 Minutes!

### ✅ What You'll Get
- YouGen AI
- Professional web application
- Ready-to-deploy code
- Complete documentation

### 🎯 Quick Start (3 Steps)

#### Step 1: Extract Files
```bash
# Extract the downloaded ZIP file
unzip yougenai-ai-youtube-generator.zip
cd yougenai-ai-youtube-generator
```

#### Step 2: Run Setup Script
```bash
# Make setup script executable
chmod +x setup.sh

# Run the automated setup
./setup.sh
```

#### Step 3: Start Using
```bash
# Start the application
python app.py
```

**Open your browser and go to: http://localhost:5000**

### 🖥️ System Requirements
- **Operating System**: Windows 10+, macOS 10.14+, or Linux
- **Python**: 3.8 or higher (automatically installed by setup script)
- **Internet**: Required for AI model download
- **Storage**: 1GB free space

### 🔧 Manual Installation (If Setup Script Fails)

#### Windows Users:
1. Install Python from https://python.org
2. Open Command Prompt in the project folder
3. Run: `pip install -r requirements.txt`
4. Download Ollama from https://ollama.ai/download
5. Run: `ollama pull gemma:2b`
6. Run: `python app.py`

#### macOS/Linux Users:
```bash
# Install Python dependencies
pip3 install -r requirements.txt

# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Download AI model
ollama pull gemma:2b

# Start the application
python3 app.py
```

### 🌐 Deploy to Web (Optional)

#### Deploy to Heroku (Free):
```bash
# Install Heroku CLI from https://devcenter.heroku.com/articles/heroku-cli
heroku create your-app-name
git add .
git commit -m "Initial commit"
git push heroku main
```

#### Deploy to Railway (Free):
1. Go to https://railway.app
2. Connect your GitHub repository
3. Deploy automatically

### 🎬 How to Use

1. **Enter Video Topic**: Describe what your video is about
2. **Choose Tone**: Select Professional, Casual, Humorous, etc.
3. **Pick Audience**: Target Teens, Adults, Professionals, etc.
4. **Click Generate**: Get instant AI-generated content
5. **Copy & Use**: Copy the titles, descriptions, and hashtags

### 🆘 Need Help?

- **Documentation**: See README.md for detailed guide
- **Video Tutorial**: Check the included demo.mp4
- **Support**: Contact us at support@yougenai.com

### 🎉 You're Ready!

Your YouGen AI is now running! Create viral content for your YouTube channel in seconds.

---

**Enjoy your new AI-powered YouTube success! 🚀** 

---

**Additional Notes:**

1. **Secret Key Configuration:**
   - Ensure you have a `.env` file in the project directory with the following content:
     ```
     SECRET_KEY=your-secret-key
     FLASK_DEBUG=True
     PORT=5000
     ```

2. **Manual Installation Steps:**
   - After installing Python and Ollama, follow these steps:
     - Create and activate a virtual environment:
       - Windows:
         ```
         python -m venv venv
         venv\Scripts\activate
         ```
       - macOS/Linux:
         ```
         python3 -m venv venv
         source venv/bin/activate
         ```
     - Install dependencies:
       ```
       pip install -r requirements.txt
       ```
     - Download the AI model:
       ```
       ollama pull gemma:2b
       ```
     - Create a `.env` file (if not present):
       ```
       SECRET_KEY=your-secret-key
       FLASK_DEBUG=True
       PORT=5000
       ```
     - Start the application:
       ```
       python app.py
       ```
   - Open [http://localhost:5000](http://localhost:5000) in your browser.

3. **For more details, see the INSTALLATION.md and README.md files included in your download.**  
   If you have any issues, check SUPPORT.md or contact support@yougenai.com.
 