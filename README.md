# 🎬 YouGen AI - YouTube Content Generator

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1.1-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](docs/LICENSE.txt)
[![Deploy](https://img.shields.io/badge/Deploy-Heroku-purple.svg)](https://heroku.com)

> **Transform Your YouTube Channel with AI-Powered Content Generation**

YouGen AI is a professional-grade AI application that instantly generates viral YouTube titles, descriptions, hashtags, and thumbnail ideas. Built with cutting-edge AI technology, it helps content creators, marketers, and businesses boost their YouTube presence and maximize engagement.

## 📋 Table of Contents

- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Customization](#-customization)
- [Deployment](#-deployment)
- [File Structure](#-file-structure)
- [Support](#-support)
- [License](#-license)

## ✨ Features

### 🎯 Core Capabilities
- **AI-Powered Title Generation**: Create compelling, SEO-optimized YouTube titles
- **Smart Description Writer**: Generate engaging video descriptions that boost CTR
- **Trending Hashtag Generator**: Get relevant, trending hashtags for maximum reach
- **Thumbnail Idea Creator**: Brainstorm eye-catching thumbnail concepts
- **Tone Customization**: Match your brand voice with multiple tone options
- **Audience Targeting**: Tailor content for specific demographics

### 🚀 Advanced Features
- **Real-time AI Processing**: Instant content generation using Ollama AI
- **Responsive Web Interface**: Beautiful, mobile-friendly design
- **Production Ready**: Built for scalability and reliability
- **Easy Deployment**: One-click deployment to major platforms
- **Health Monitoring**: Built-in health checks and error handling

## 📋 Requirements

### System Requirements
- **Python**: 3.8 or higher
- **RAM**: Minimum 2GB (4GB recommended)
- **Storage**: 500MB free space
- **Internet**: Required for AI model access

### Software Dependencies
- **Ollama**: Local AI model server
- **Flask**: Web framework
- **Gunicorn**: Production WSGI server
- **Python-dotenv**: Environment management

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd yougen_ai_converter-main
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r config/requirements.txt
```

### 4. Install Ollama
Visit [ollama.ai](https://ollama.ai) and follow the installation instructions for your platform.

### 5. Download AI Model
```bash
ollama pull gemma2:2b
```

## ⚙️ Configuration

### 1. Environment Variables
Create a `.env` file in the project root:

```env
# Flask Configuration
SECRET_KEY=your-secret-key-here
FLASK_DEBUG=False
FLASK_ENV=production

# AI Configuration
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=gemma2:2b

# Database Configuration (if needed)
DATABASE_URL=your-database-url

# External Services
API_KEY=your-api-key
```

### 2. Generate Secret Key
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

## 🚀 Usage

### 1. Start the Application
```bash
python main.py
```

### 2. Access the Application
Open your web browser and navigate to `http://localhost:5000`

### 3. Generate Content
1. **Enter Video Topic**: Describe your video content in detail
2. **Select Tone**: Choose from Professional, Casual, Humorous, Educational, etc.
3. **Choose Audience**: Target specific demographics (Teens, Adults, Professionals, etc.)
4. **Click Generate**: AI will create content instantly

### 4. Use Generated Content
- **Titles**: Copy and paste the best title option
- **Descriptions**: Use the generated description as a base and customize
- **Hashtags**: Include relevant hashtag groups in your video description
- **Thumbnails**: Use the ideas as inspiration for your thumbnail design

## 🎨 Customization

### 1. Styling and Themes
Edit the CSS files in `assets/css/` to customize the appearance:
- `main.css`: Main stylesheet
- `responsive.css`: Mobile responsiveness
- `themes.css`: Color themes and variations

### 2. AI Prompts
Modify AI prompts in `src/controllers/app.py`:
- Title generation prompts
- Description generation prompts
- Hashtag generation prompts
- Thumbnail idea prompts

### 3. Templates
Customize HTML templates in `src/views/`:
- `index.html`: Main application interface
- `blog_post.html`: Blog post template
- `404.html` and `500.html`: Error pages

### 4. Configuration
Update settings in `config/config.py`:
- Product information
- Default values
- Feature toggles

## 🌐 Deployment

### Deploy to Heroku
1. Install Heroku CLI
2. Create Heroku app:
```bash
heroku create your-app-name
```

3. Set environment variables:
```bash
heroku config:set SECRET_KEY=$(python -c "import secrets; print(secrets.token_hex(32))")
heroku config:set FLASK_DEBUG=False
```

4. Deploy:
```bash
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

### Deploy to Railway
1. Connect your GitHub repository to Railway
2. Set environment variables in Railway dashboard
3. Deploy automatically

### Deploy to Render
1. Create new Web Service on Render
2. Connect GitHub repository
3. Set build command: `pip install -r config/requirements.txt`
4. Set start command: `gunicorn main:app`
5. Set environment variables

## 📁 File Structure

```
yougen_ai_converter-main/
├── main.py                 # Main application entry point
├── README.md              # This file
├── assets/                # Static assets
│   ├── css/              # Stylesheets
│   ├── js/               # JavaScript files
│   ├── images/           # Images and media
│   │   ├── blog/         # Blog images
│   │   └── screenshots/  # Application screenshots
│   └── fonts/            # Custom fonts
├── src/                   # Source code
│   ├── controllers/      # Flask routes and logic
│   │   └── app.py        # Main Flask application
│   ├── views/            # HTML templates
│   │   ├── index.html    # Main page
│   │   ├── blog_post.html
│   │   ├── 404.html
│   │   └── 500.html
│   ├── models/           # Data models (if needed)
│   └── utils/            # Utility functions
│       ├── test_app.py
│       ├── test_sitemap.py
│       ├── blog_images.py
│       └── sitemap.xml
├── config/               # Configuration files
│   ├── config.py         # Application configuration
│   ├── requirements.txt  # Python dependencies
│   ├── Procfile         # Heroku deployment
│   ├── runtime.txt      # Python runtime
│   ├── .gitignore       # Git ignore rules
│   ├── deploy.sh        # Deployment script
│   ├── setup.sh         # Setup script
│   ├── setup.bat        # Windows setup script
│   ├── start.sh         # Start script
│   └── stop.sh          # Stop script
└── docs/                # Documentation
    ├── LICENSE.txt      # License file
    ├── CHANGELOG.md     # Version history
    ├── DEMO.md          # Demo instructions
    ├── INSTALLATION.md  # Detailed installation
    ├── SUPPORT.md       # Support information
    ├── RETURN_POLICY_CONFIG.md
    ├── attribution.txt  # Asset attributions
    └── DOCUMENTATION.html
```

## 🆘 Support

### Documentation
- **Installation Guide**: See `docs/INSTALLATION.md`
- **Demo Instructions**: See `docs/DEMO.md`
- **Support Information**: See `docs/SUPPORT.md`

### Common Issues

#### 1. Ollama Connection Error
**Problem**: Cannot connect to Ollama server
**Solution**: 
- Ensure Ollama is running: `ollama serve`
- Check if model is downloaded: `ollama list`
- Verify OLLAMA_HOST in environment variables

#### 2. Flask Import Errors
**Problem**: Module not found errors
**Solution**:
- Ensure you're in the project root directory
- Activate virtual environment
- Install dependencies: `pip install -r config/requirements.txt`

#### 3. Port Already in Use
**Problem**: Port 5000 is already occupied
**Solution**:
- Change port in `main.py`
- Or kill existing process: `lsof -ti:5000 | xargs kill -9`

### Getting Help
- **Email**: support@yougenai.com
- **Documentation**: Check `docs/` folder
- **Issues**: Create an issue on GitHub

## 📄 License

This project is licensed under the MIT License - see `docs/LICENSE.txt` for details.

## 🙏 Acknowledgments

- **Ollama**: For providing the AI model infrastructure
- **Flask**: For the web framework
- **Tailwind CSS**: For the beautiful UI components
- **Font Awesome**: For the icons

## 🔄 Changelog

See `docs/CHANGELOG.md` for a complete list of changes and version history.

---

**Made with ❤️ for content creators worldwide** 