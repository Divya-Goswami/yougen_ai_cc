#!/usr/bin/env python3
"""
YouGen AI - YouTube Content Generator
Setup Script

This script sets up the YouGen AI application for development and production use.
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()

# Read requirements
def read_requirements():
    with open('config/requirements.txt', 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="yougen-ai",
    version="1.0.0",
    author="YouGen AI Team",
    author_email="support@yougenai.com",
    description="AI-powered YouTube content generator for titles, descriptions, hashtags, and thumbnail ideas",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://yougenai.com",
    project_urls={
        "Bug Tracker": "https://github.com/yougenai/yougen-ai/issues",
        "Documentation": "https://docs.yougenai.com",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Video",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.8",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-flask>=1.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
        ],
        "production": [
            "gunicorn>=20.0.0",
            "gevent>=21.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "yougen-ai=main:main",
        ],
    },
    keywords="youtube, ai, content-generation, flask, ollama, titles, descriptions, hashtags",
    zip_safe=False,
) 