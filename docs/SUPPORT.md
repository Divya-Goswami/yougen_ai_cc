# 🆘 Support Guide - YouGen AI YouTube Content Generator

## 📞 Getting Help

### 🎯 Quick Support Options
- **📧 Email**: support@YouGen.com
- **🌐 Website**: https://YouGen.com/support
- **📚 Documentation**: See README.md for complete guide
- **🎬 Demo**: See DEMO.md for usage examples

### ⏰ Response Times
- **Email Support**: 24-48 hours
- **Documentation**: Instant access
- **Community**: Real-time discussions

---

## 🔧 Common Issues & Solutions

### ❌ Installation Problems

#### Issue: "Python not found"
**Solution**:
```bash
# Windows: Download from https://python.org
# macOS: brew install python3
# Linux: sudo apt-get install python3
```

#### Issue: "Ollama not found"
**Solution**:
```bash
# macOS/Linux:
curl -fsSL https://ollama.ai/install.sh | sh

# Windows: Download from https://ollama.ai/download
```

#### Issue: "Port 5000 already in use"
**Solution**:
```bash
# Find the process
lsof -i :5000  # macOS/Linux
netstat -ano | findstr :5000  # Windows

# Kill the process
kill -9 <PID>  # macOS/Linux
taskkill /PID <PID> /F  # Windows
```

#### Issue: "Setup script fails"
**Solution**:
1. Check Python version (3.8+ required)
2. Ensure internet connection
3. Try manual installation from INSTALLATION.md
4. Contact support with error details

### ❌ Runtime Problems

#### Issue: "AI model not responding"
**Solution**:
```bash
# Restart Ollama
pkill ollama
ollama serve

# Check model availability
ollama list

# Re-download model if needed
ollama pull gemma:2b
```

#### Issue: "Application won't start"
**Solution**:
```bash
# Check virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt

# Check .env file exists
ls -la .env
```

#### Issue: "Content generation fails"
**Solution**:
1. Check Ollama is running: `curl http://localhost:11434/api/tags`
2. Verify model is downloaded: `ollama list`
3. Check internet connection
4. Try different input parameters

### ❌ Performance Issues

#### Issue: "Slow content generation"
**Solution**:
- Ensure sufficient RAM (2GB+ recommended)
- Close other applications
- Use smaller AI model if needed
- Check system resources

#### Issue: "High memory usage"
**Solution**:
- Restart the application periodically
- Use smaller AI models
- Increase system RAM
- Monitor with task manager

---

## 🛠️ Troubleshooting Steps

### Step 1: Check System Requirements
```bash
# Check Python version
python --version

# Check available memory
free -h  # Linux
top       # macOS
taskmgr   # Windows

# Check disk space
df -h     # Linux/macOS
dir       # Windows
```

### Step 2: Verify Installation
```bash
# Check if all files exist
ls -la

# Verify virtual environment
ls -la venv/

# Check dependencies
pip list
```

### Step 3: Test Components
```bash
# Test Python
python -c "print('Python works')"

# Test Ollama
ollama list

# Test Flask
python -c "import flask; print('Flask works')"
```

### Step 4: Check Logs
```bash
# Check application logs
tail -f app.log  # if logging is enabled

# Check system logs
dmesg | tail     # Linux
log show --last 1m  # macOS
```

---

## 📋 Diagnostic Information

When contacting support, please include:

### System Information
```bash
# Operating System
uname -a  # Linux/macOS
systeminfo  # Windows

# Python Version
python --version

# Available Memory
free -h  # Linux
vm_stat  # macOS
wmic computersystem get TotalPhysicalMemory  # Windows
```

### Application Information
```bash
# Installed Dependencies
pip freeze

# Ollama Models
ollama list

# Environment Variables
cat .env
```

### Error Details
- Exact error message
- Steps to reproduce
- Screenshots if applicable
- Browser console logs (if web-related)

---

## 🔄 Reinstallation Guide

### Complete Reset
```bash
# Stop all processes
pkill -f "python.*app.py"
pkill ollama

# Remove old installation
rm -rf venv
rm -f .env
rm -f start.sh stop.sh

# Reinstall
./setup.sh
```

### Windows Reset
```cmd
# Stop processes
taskkill /f /im python.exe
taskkill /f /im ollama.exe

# Remove old files
rmdir /s /q venv
del .env
del start.bat
del stop.bat

# Reinstall
setup.bat
```

---

## 🌐 Deployment Support

### Heroku Issues
```bash
# Check Heroku logs
heroku logs --tail

# Restart application
heroku restart

# Check environment variables
heroku config
```

### Railway Issues
- Check Railway dashboard for logs
- Verify environment variables
- Restart deployment if needed

### Render Issues
- Check Render dashboard for logs
- Verify build settings
- Check environment variables

---

## 📚 Additional Resources

### Documentation
- **[README.md](README.md)**: Complete documentation
- **[INSTALLATION.md](INSTALLATION.md)**: Installation guide
- **[DEMO.md](DEMO.md)**: Usage examples
- **[CHANGELOG.md](CHANGELOG.md)**: Version history

### External Resources
- **[Flask Documentation](https://flask.palletsprojects.com/)**: Web framework docs
- **[Ollama Documentation](https://ollama.ai/docs)**: AI model docs
- **[Python Documentation](https://docs.python.org/)**: Python language docs

### Community Support
- **GitHub Issues**: Report bugs and request features
- **Stack Overflow**: Search for similar problems
- **Reddit**: r/Python, r/Flask communities

---

## 🎯 Pro Tips

### Performance Optimization
1. **Use SSD storage** for faster model loading
2. **Increase RAM** for better performance
3. **Close unnecessary applications** during use
4. **Restart periodically** to clear memory

### Content Quality
1. **Be specific** with video topics
2. **Experiment with different tones**
3. **Target specific audiences**
4. **Customize generated content**

### Troubleshooting
1. **Check logs first** before contacting support
2. **Try simple examples** to isolate issues
3. **Update regularly** for latest fixes
4. **Backup your data** before major changes

---

## 📞 Contact Information

### Support Channels
- **📧 Email**: support@YouGen.com
- **🌐 Website**: https://YouGen.com
- **📱 Social**: @YouGen on Twitter
- **💬 Chat**: Live chat on website

### Business Hours
- **Monday - Friday**: 9 AM - 6 PM EST
- **Saturday**: 10 AM - 4 PM EST
- **Sunday**: Closed

### Priority Support
- **Pro Users**: 12-hour response time
- **Enterprise Users**: 4-hour response time
- **Free Users**: 48-hour response time

---

*We're here to help you succeed with YouGen! 🚀* 