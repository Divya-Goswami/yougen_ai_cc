# YouGen AI - YouTube Content Generator
## CodeCanyon Documentation

### Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Customization](#customization)
6. [Usage](#usage)
7. [Troubleshooting](#troubleshooting)
8. [Support](#support)

---

## Introduction

YouGen AI is a professional-grade AI application that generates viral YouTube titles, descriptions, hashtags, and thumbnail ideas. This application is built with Flask and uses Ollama AI for content generation.

### What You Get
- Complete Flask web application
- AI-powered content generation
- Responsive web interface
- Production-ready deployment scripts
- Comprehensive documentation

---

## Features

### Core Features
- **AI Title Generation**: Create compelling YouTube titles
- **Description Writer**: Generate engaging video descriptions
- **Hashtag Generator**: Get trending hashtags for maximum reach
- **Thumbnail Ideas**: Brainstorm eye-catching thumbnail concepts
- **Tone Customization**: Multiple tone options (Professional, Casual, Humorous, etc.)
- **Audience Targeting**: Target specific demographics

### Technical Features
- Responsive design (mobile-friendly)
- Real-time AI processing
- Health monitoring
- Error handling
- Easy deployment options

---

## Installation

### Prerequisites
- Python 3.8 or higher
- 2GB RAM minimum (4GB recommended)
- 500MB free disk space
- Internet connection

### Step 1: Extract Files
1. Download the ZIP file from CodeCanyon
2. Extract to your desired location
3. Open terminal/command prompt in the extracted folder

### Step 2: Install Python Dependencies
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r config/requirements.txt
```

### Step 3: Install Ollama
1. Visit [ollama.ai](https://ollama.ai)
2. Download and install Ollama for your platform
3. Open terminal and run:
```bash
ollama pull gemma2:2b
```

### Step 4: Configure Environment
1. Create a `.env` file in the project root
2. Add the following content:
```env
SECRET_KEY=your-secret-key-here
FLASK_DEBUG=False
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=gemma2:2b
```

### Step 5: Start the Application
```bash
# Start Ollama (in a separate terminal)
ollama serve

# Start the application
python main.py
```

### Step 6: Access the Application
Open your web browser and go to: `http://localhost:5000`

---

## Configuration

### Environment Variables
Edit the `.env` file to customize your application:

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Flask secret key | Auto-generated |
| `FLASK_DEBUG` | Debug mode | False |
| `OLLAMA_HOST` | Ollama server URL | http://localhost:11434 |
| `OLLAMA_MODEL` | AI model name | gemma2:2b |

### Application Settings
Edit `config/config.py` to modify:
- Product information
- Default values
- Feature toggles
- AI prompts

---

## Customization

### 1. Styling and Themes

#### Modify CSS
Edit files in `assets/css/`:
- `main.css`: Main stylesheet
- `responsive.css`: Mobile responsiveness
- `themes.css`: Color themes

#### Color Scheme
To change colors, edit `assets/css/themes.css`:
```css
:root {
    --primary-color: #your-color;
    --secondary-color: #your-color;
    --accent-color: #your-color;
}
```

#### Fonts
1. Add custom fonts to `assets/fonts/`
2. Update `assets/css/main.css`:
```css
@font-face {
    font-family: 'YourFont';
    src: url('../fonts/your-font.woff2') format('woff2');
}
```

### 2. AI Prompts
Edit `src/controllers/app.py` to customize AI prompts:

#### Title Generation
Find the `generate_titles` function and modify the prompt:
```python
def generate_titles(topic, tone, audience):
    prompt = f"""
    Generate 5 viral YouTube titles for: {topic}
    Tone: {tone}
    Audience: {audience}
    Make them catchy and SEO-optimized.
    """
```

#### Description Generation
Find the `generate_description` function and modify:
```python
def generate_description(topic, tone, audience):
    prompt = f"""
    Write an engaging YouTube description for: {topic}
    Tone: {tone}
    Audience: {audience}
    Include call-to-action and relevant keywords.
    """
```

### 3. Templates
Edit HTML templates in `src/views/`:

#### Main Page (`index.html`)
- Modify the form fields
- Change layout and styling
- Add custom sections

#### Blog Template (`blog_post.html`)
- Customize blog post layout
- Add social sharing buttons
- Modify meta tags

### 4. Adding New Features

#### New AI Generation Type
1. Add new route in `src/controllers/app.py`:
```python
@app.route('/generate/new-feature', methods=['POST'])
def generate_new_feature():
    # Your generation logic here
    pass
```

2. Add form field in `src/views/index.html`:
```html
<div class="form-group">
    <label for="new-feature">New Feature</label>
    <input type="text" id="new-feature" name="new-feature">
</div>
```

#### New Tone Options
Edit `src/views/index.html` and add to the tone select:
```html
<option value="new-tone">New Tone</option>
```

---

## Usage

### Basic Usage
1. **Enter Video Topic**: Describe your video content in detail
2. **Select Tone**: Choose from available tone options
3. **Choose Audience**: Select target demographic
4. **Click Generate**: AI will create content instantly
5. **Copy Results**: Use the generated content for your YouTube videos

### Advanced Usage
- **Batch Generation**: Generate multiple variations
- **Custom Prompts**: Modify AI prompts for specific needs
- **Export Results**: Copy and save generated content

### Best Practices
- Be specific with video topics
- Use relevant tone for your audience
- Combine multiple generated options
- Customize generated content before using

---

## Troubleshooting

### Common Issues

#### 1. "Cannot connect to Ollama"
**Solution**:
- Ensure Ollama is running: `ollama serve`
- Check if model is downloaded: `ollama list`
- Verify OLLAMA_HOST in `.env` file

#### 2. "Module not found" errors
**Solution**:
- Activate virtual environment
- Install dependencies: `pip install -r config/requirements.txt`
- Check Python version (3.8+ required)

#### 3. "Port 5000 already in use"
**Solution**:
- Change port in `main.py`
- Or kill existing process:
```bash
# On macOS/Linux:
lsof -ti:5000 | xargs kill -9
# On Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

#### 4. "Permission denied" errors
**Solution**:
- Check file permissions
- Run as administrator (Windows)
- Use `sudo` (macOS/Linux)

### Performance Issues
- **Slow generation**: Ensure sufficient RAM (4GB+ recommended)
- **High CPU usage**: Close other applications
- **Memory errors**: Restart Ollama server

### AI Model Issues
- **Poor quality results**: Try different models
- **Timeout errors**: Increase timeout in configuration
- **Model not found**: Download model: `ollama pull gemma2:2b`

---

## Deployment

### Local Development
```bash
python main.py
```

### Production Deployment

#### Heroku
1. Install Heroku CLI
2. Create app: `heroku create your-app-name`
3. Set environment variables:
```bash
heroku config:set SECRET_KEY=$(python -c "import secrets; print(secrets.token_hex(32))")
heroku config:set FLASK_DEBUG=False
```
4. Deploy: `git push heroku main`

#### Railway
1. Connect GitHub repository
2. Set environment variables in dashboard
3. Deploy automatically

#### Render
1. Create Web Service
2. Connect repository
3. Set build command: `pip install -r config/requirements.txt`
4. Set start command: `gunicorn main:app`

### Environment Variables for Production
```env
SECRET_KEY=your-production-secret-key
FLASK_DEBUG=False
FLASK_ENV=production
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=gemma2:2b
```

---

## Support

### Documentation Files
- `README.md`: Main documentation
- `docs/INSTALLATION.md`: Detailed installation guide
- `docs/DEMO.md`: Demo instructions
- `docs/SUPPORT.md`: Support information

### Getting Help
1. **Check Documentation**: Review all documentation files
2. **Common Issues**: See troubleshooting section above
3. **Code Comments**: Check code comments for guidance
4. **Contact Support**: Email support@yougenai.com

### File Structure Reference
```
yougen_ai_converter-main/
├── main.py                 # Start here
├── assets/                 # CSS, JS, images
├── src/                    # Application code
│   ├── controllers/       # Main logic
│   ├── views/            # HTML templates
│   └── utils/            # Helper functions
├── config/                # Configuration files
└── docs/                  # Documentation
```

---

## License and Attribution

### License
This item is licensed under the MIT License. See `docs/LICENSE.txt` for details.

### Third-Party Assets
- **Ollama**: AI model infrastructure
- **Flask**: Web framework
- **Tailwind CSS**: UI components
- **Font Awesome**: Icons

### Attribution Requirements
If you use this item, please include attribution to the original author in your project documentation.

---

**Thank you for purchasing YouGen AI!**

For additional support, please refer to the documentation files or contact our support team. 