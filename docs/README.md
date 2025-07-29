# 🎬 YouGen AI

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1.1-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.txt)
[![Deploy](https://img.shields.io/badge/Deploy-Heroku-purple.svg)](https://heroku.com)

> **Transform Your YouTube Channel with AI-Powered Content Generation**

YouGen AI is a professional-grade AI application that instantly generates viral YouTube titles, descriptions, hashtags, and thumbnail ideas. Built with cutting-edge AI technology, it helps content creators, marketers, and businesses boost their YouTube presence and maximize engagement.

## 🚀 Features

### ✨ Core Capabilities
- **AI-Powered Title Generation**: Create compelling, SEO-optimized YouTube titles
- **Smart Description Writer**: Generate engaging video descriptions that boost CTR
- **Trending Hashtag Generator**: Get relevant, trending hashtags for maximum reach
- **Thumbnail Idea Creator**: Brainstorm eye-catching thumbnail concepts
- **Tone Customization**: Match your brand voice with multiple tone options
- **Audience Targeting**: Tailor content for specific demographics

### 🎯 Advanced Features
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

## 🛠️ Installation Guide

_KEY=$(python -c "import secrets; print(secrets.token_hex(32))")
heroku config:set FLASK_DEBUG=False

# Deploy
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

#### Deploy to Railway
1. Connect your GitHub repository to Railway
2. Set environment variables:
   - `SECRET_KEY`: Generate with `python -c "import secrets; print(secrets.token_hex(32))"`
   - `FLASK_DEBUG`: `False`
3. Deploy automatically

#### Deploy to Render
1. Create new Web Service on Render
2. Connect GitHub repository
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `gunicorn app:app`
5. Set environment variables as above

## 📖 Usage Guide

### 1. Access the Application
Open your web browser and navigate to the deployed URL or `http://localhost:5000`

### 2. Generate Content
1. **Enter Video Topic**: Describe your video content in detail
2. **Select Tone**: Choose from Professional, Casual, Humorous, Educational, etc.
3. **Choose Audience**: Target specific demographics (Teens, Adults, Professionals, etc.)
4. **Click Generate**: AI will create content instantly

### 3. Use Generated Content
- **Titles**: Copy and paste the best title option
- **Descriptions**: Use the generated description as a base and customize
- **Hashtags**: Include relevant hashtag groups in your video description
- **Thumbnails**: Use the ideas as inspiration for your thumbnail design

## 🏗️ Architecture

### Technology Stack
- **Backend**: Flask (Python web framework)
- **AI Engine**: Ollama with Gemma 2B model
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Deployment**: Gunicorn WSGI server
- **Environment**: Python virtual environment

### File Structure
```
ai-youtube-content-generator/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku deployment config
├── deploy.sh             # Automated deployment script
├── templates/            # HTML templates
│   ├── index.html        # Main application interface
│   ├── 404.html          # Error page
│   └── 500.html          # Server error page
├── venv/                 # Python virtual environment
└── README.md             # This file
```

## 🔧 Configuration

### Environment Variables
| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `SECRET_KEY` | Flask secret key | `your-secret-key-change-in-production` | Yes |
| `FLASK_DEBUG` | Debug mod### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/ai-youtube-content-generator.git
cd ai-youtube-content-generator
```

### Step 2: Set Up Python Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Install Ollama
```bash
# On macOS/Linux:
curl -fsSL https://ollama.ai/install.sh | sh

# On Windows:
# Download from https://ollama.ai/download
```

### Step 5: Download AI Model
```bash
# Start Ollama service
ollama serve

# In a new terminal, pull the model
ollama pull gemma:2b
```

### Step 6: Configure Environment
```bash
# Create .env file
cat > .env << EOF
SECRET_KEY=your-secret-key-change-in-production
FLASK_DEBUG=True
PORT=5000
EOF
```

### Step 7: Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 🚀 Quick Deployment

### Option 1: Automated Deployment Script
```bash
chmod +x deploy.sh
./deploy.sh
```

### Option 2: Manual Deployment

#### Deploy to Heroku
```bash
# Install Heroku CLI
# Create app
heroku create your-app-name

# Set environment variables
heroku config:set SECRETe | `False` | No |
| `PORT` | Server port | `5000` | No |

### AI Model Configuration
The application uses the Gemma 2B model through Ollama. You can switch to other models by modifying the `model` parameter in `app.py`:

```python
response = ollama.chat(
    model='gemma:2b',  # Change this to use different models
    messages=[{"role": "user", "content": prompt}]
)
```

## 🧪 Testing

### Health Check
```bash
curl http://localhost:5000/health
```

### Manual Testing
1. Start the application
2. Navigate to the web interface
3. Enter test data and verify content generation
4. Check error handling with invalid inputs

## 🔒 Security Considerations

### Production Deployment
1. **Change Secret Key**: Always update `SECRET_KEY` in production
2. **Disable Debug Mode**: Set `FLASK_DEBUG=False`
3. **Use HTTPS**: Enable SSL/TLS encryption
4. **Rate Limiting**: Implement rate limiting for API endpoints
5. **Input Validation**: Validate all user inputs

### Environment Security
- Never commit `.env` files to version control
- Use environment variables for sensitive data
- Regularly update dependencies for security patches

## 🐛 Troubleshooting

### Common Issues

#### Ollama Not Running
```bash
# Start Ollama service
ollama serve

# Check if model is available
ollama list
```

#### Port Already in Use
```bash
# Find process using port 5000
lsof -i :5000

# Kill the process
kill -9 <PID>
```

#### Python Dependencies Issues
```bash
# Reinstall dependencies
pip uninstall -r requirements.txt
pip install -r requirements.txt
```

#### Virtual Environment Issues
```bash
# Recreate virtual environment
rm -rf venv
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## 📈 Performance Optimization

### For High Traffic
1. **Use Production WSGI**: Gunicorn is already configured
2. **Enable Caching**: Implement Redis for session storage
3. **Load Balancing**: Use multiple worker processes
4. **CDN**: Serve static assets through CDN

### AI Model Optimization
1. **Model Selection**: Choose appropriate model size for your needs
2. **Response Caching**: Cache common queries
3. **Async Processing**: Implement background tasks for long-running operations

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Code Style
- Follow PEP 8 Python style guide
- Use meaningful variable names
- Add comments for complex logic
- Write docstrings for functions

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## 🆘 Support

### Documentation
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Ollama Documentation](https://ollama.ai/docs)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)

### Community
- GitHub Issues: Report bugs and request features
- Discussions: Ask questions and share ideas

### Professional Support
For enterprise support and custom development, contact us at:
- Email: divya.gusai7893@gmail.com
## 🎯 Roadmap

### Upcoming Features
- [ ] Multiple AI model support
- [ ] Content scheduling integration
- [ ] Analytics dashboard
- [ ] Team collaboration features
- [ ] API endpoints for third-party integration
- [ ] Mobile application
- [ ] Advanced SEO optimization
- [ ] Content performance tracking

### Version History
- **v1.0.0**: Initial release with core content generation
- **v1.1.0**: Added thumbnail ideas and improved UI
- [ ] Team collaboration features

---

**Ready to transform your YouTube channel? Get started with YouGen AI today!** 🚀

*Built with ❤️ for content creators worldwide*
