/**
 * YouGen AI - Main JavaScript
 * Handles interactive functionality for the YouTube content generator
 */

class YouGenAI {
    constructor() {
        this.initializeEventListeners();
        this.setupCopyButtons();
        this.setupFormValidation();
    }

    /**
     * Initialize all event listeners
     */
    initializeEventListeners() {
        // Form submission
        const form = document.getElementById('content-form');
        if (form) {
            form.addEventListener('submit', (e) => this.handleFormSubmit(e));
        }

        // Tone selection
        const toneSelect = document.getElementById('tone');
        if (toneSelect) {
            toneSelect.addEventListener('change', (e) => this.handleToneChange(e));
        }

        // Audience selection
        const audienceSelect = document.getElementById('audience');
        if (audienceSelect) {
            audienceSelect.addEventListener('change', (e) => this.handleAudienceChange(e));
        }

        // Clear results button
        const clearBtn = document.getElementById('clear-results');
        if (clearBtn) {
            clearBtn.addEventListener('click', () => this.clearResults());
        }

        // Generate more button
        const generateMoreBtn = document.getElementById('generate-more');
        if (generateMoreBtn) {
            generateMoreBtn.addEventListener('click', () => this.generateMore());
        }
    }

    /**
     * Handle form submission
     */
    async handleFormSubmit(e) {
        e.preventDefault();
        
        const form = e.target;
        const formData = new FormData(form);
        
        // Validate form
        if (!this.validateForm(formData)) {
            return;
        }

        // Show loading state
        this.showLoading();
        
        try {
            const response = await fetch('/', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const result = await response.json();
            this.displayResults(result);
            
        } catch (error) {
            console.error('Error:', error);
            this.showError('An error occurred while generating content. Please try again.');
        } finally {
            this.hideLoading();
        }
    }

    /**
     * Validate form data
     */
    validateForm(formData) {
        const topic = formData.get('topic');
        const tone = formData.get('tone');
        const audience = formData.get('audience');

        if (!topic || topic.trim().length < 10) {
            this.showError('Please provide a detailed video topic (at least 10 characters).');
            return false;
        }

        if (!tone) {
            this.showError('Please select a tone for your content.');
            return false;
        }

        if (!audience) {
            this.showError('Please select a target audience.');
            return false;
        }

        return true;
    }

    /**
     * Display generated results
     */
    displayResults(data) {
        const resultsContainer = document.getElementById('results');
        if (!resultsContainer) return;

        resultsContainer.innerHTML = '';

        // Display titles
        if (data.titles && data.titles.length > 0) {
            this.createResultSection(resultsContainer, 'Titles', data.titles, 'title');
        }

        // Display descriptions
        if (data.description && data.description.length > 0) {
            this.createResultSection(resultsContainer, 'Descriptions', data.description, 'description');
        }

        // Display hashtags
        if (data.hashtags && data.hashtags.length > 0) {
            this.createResultSection(resultsContainer, 'Hashtags', data.hashtags, 'hashtag');
        }

        // Display thumbnail ideas
        if (data.thumbnails && data.thumbnails.length > 0) {
            this.createResultSection(resultsContainer, 'Thumbnail Ideas', data.thumbnails, 'thumbnail');
        }

        // Show results container
        resultsContainer.style.display = 'block';
        
        // Scroll to results
        resultsContainer.scrollIntoView({ behavior: 'smooth' });
    }

    /**
     * Create a result section
     */
    createResultSection(container, title, items, type) {
        const section = document.createElement('div');
        section.className = 'result-section';

        const sectionTitle = document.createElement('h3');
        sectionTitle.className = 'result-title';
        sectionTitle.innerHTML = `
            <i class="fas fa-${this.getIconForType(type)}"></i>
            ${title}
        `;

        section.appendChild(sectionTitle);

        items.forEach((item, index) => {
            const resultItem = document.createElement('div');
            resultItem.className = 'result-item';

            const resultText = document.createElement('div');
            resultText.className = 'result-text';
            resultText.textContent = item;

            const actions = document.createElement('div');
            actions.className = 'result-actions';

            const copyBtn = document.createElement('button');
            copyBtn.className = 'btn-copy';
            copyBtn.textContent = 'Copy';
            copyBtn.onclick = () => this.copyToClipboard(item);

            const saveBtn = document.createElement('button');
            saveBtn.className = 'btn-copy';
            saveBtn.textContent = 'Save';
            saveBtn.onclick = () => this.saveItem(item, type, index);

            actions.appendChild(copyBtn);
            actions.appendChild(saveBtn);

            resultItem.appendChild(resultText);
            resultItem.appendChild(actions);
            section.appendChild(resultItem);
        });

        container.appendChild(section);
    }

    /**
     * Get icon for result type
     */
    getIconForType(type) {
        const icons = {
            title: 'heading',
            description: 'file-text',
            hashtag: 'hashtag',
            thumbnail: 'image'
        };
        return icons[type] || 'star';
    }

    /**
     * Copy text to clipboard
     */
    async copyToClipboard(text) {
        try {
            await navigator.clipboard.writeText(text);
            this.showSuccess('Copied to clipboard!');
        } catch (err) {
            // Fallback for older browsers
            const textArea = document.createElement('textarea');
            textArea.value = text;
            document.body.appendChild(textArea);
            textArea.select();
            document.execCommand('copy');
            document.body.removeChild(textArea);
            this.showSuccess('Copied to clipboard!');
        }
    }

    /**
     * Save item to local storage
     */
    saveItem(item, type, index) {
        const savedItems = JSON.parse(localStorage.getItem('yougen_saved_items') || '[]');
        const newItem = {
            id: Date.now(),
            content: item,
            type: type,
            index: index,
            timestamp: new Date().toISOString()
        };
        
        savedItems.push(newItem);
        localStorage.setItem('yougen_saved_items', JSON.stringify(savedItems));
        
        this.showSuccess('Item saved!');
    }

    /**
     * Setup copy buttons
     */
    setupCopyButtons() {
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('btn-copy')) {
                const text = e.target.closest('.result-item').querySelector('.result-text').textContent;
                this.copyToClipboard(text);
            }
        });
    }

    /**
     * Setup form validation
     */
    setupFormValidation() {
        const topicInput = document.getElementById('topic');
        if (topicInput) {
            topicInput.addEventListener('input', (e) => {
                const value = e.target.value;
                const charCount = value.length;
                const minChars = 10;
                
                // Update character count
                const charCountEl = document.getElementById('char-count');
                if (charCountEl) {
                    charCountEl.textContent = charCount;
                    charCountEl.className = charCount < minChars ? 'text-red-500' : 'text-green-500';
                }
            });
        }
    }

    /**
     * Handle tone change
     */
    handleToneChange(e) {
        const tone = e.target.value;
        const form = document.getElementById('content-form');
        
        // Update form action or add tone parameter
        if (form) {
            form.dataset.tone = tone;
        }
    }

    /**
     * Handle audience change
     */
    handleAudienceChange(e) {
        const audience = e.target.value;
        const form = document.getElementById('content-form');
        
        // Update form action or add audience parameter
        if (form) {
            form.dataset.audience = audience;
        }
    }

    /**
     * Clear results
     */
    clearResults() {
        const resultsContainer = document.getElementById('results');
        if (resultsContainer) {
            resultsContainer.innerHTML = '';
            resultsContainer.style.display = 'none';
        }
    }

    /**
     * Generate more content
     */
    generateMore() {
        const form = document.getElementById('content-form');
        if (form) {
            form.submit();
        }
    }

    /**
     * Show loading state
     */
    showLoading() {
        const submitBtn = document.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span class="loading"></span> Generating...';
        }

        const loadingContainer = document.getElementById('loading-container');
        if (loadingContainer) {
            loadingContainer.style.display = 'flex';
        }
    }

    /**
     * Hide loading state
     */
    hideLoading() {
        const submitBtn = document.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.innerHTML = 'Generate Content';
        }

        const loadingContainer = document.getElementById('loading-container');
        if (loadingContainer) {
            loadingContainer.style.display = 'none';
        }
    }

    /**
     * Show success message
     */
    showSuccess(message) {
        this.showAlert(message, 'success');
    }

    /**
     * Show error message
     */
    showError(message) {
        this.showAlert(message, 'error');
    }

    /**
     * Show alert message
     */
    showAlert(message, type) {
        // Remove existing alerts
        const existingAlerts = document.querySelectorAll('.alert');
        existingAlerts.forEach(alert => alert.remove());

        // Create new alert
        const alert = document.createElement('div');
        alert.className = `alert alert-${type}`;
        alert.innerHTML = `
            <div class="flex items-center justify-between">
                <span>${message}</span>
                <button onclick="this.parentElement.parentElement.remove()" class="text-lg">&times;</button>
            </div>
        `;

        // Insert at top of main content
        const mainContent = document.querySelector('.main-content');
        if (mainContent) {
            mainContent.insertBefore(alert, mainContent.firstChild);
        }

        // Auto-remove after 5 seconds
        setTimeout(() => {
            if (alert.parentElement) {
                alert.remove();
            }
        }, 5000);
    }

    /**
     * Initialize saved items display
     */
    initializeSavedItems() {
        const savedItems = JSON.parse(localStorage.getItem('yougen_saved_items') || '[]');
        if (savedItems.length > 0) {
            this.displaySavedItems(savedItems);
        }
    }

    /**
     * Display saved items
     */
    displaySavedItems(items) {
        const savedContainer = document.getElementById('saved-items');
        if (!savedContainer) return;

        savedContainer.innerHTML = '<h3>Saved Items</h3>';

        items.forEach(item => {
            const itemEl = document.createElement('div');
            itemEl.className = 'result-item';
            itemEl.innerHTML = `
                <div class="result-text">${item.content}</div>
                <div class="result-actions">
                    <button class="btn-copy" onclick="yougenAI.copyToClipboard('${item.content}')">Copy</button>
                    <button class="btn-copy" onclick="yougenAI.deleteSavedItem(${item.id})">Delete</button>
                </div>
            `;
            savedContainer.appendChild(itemEl);
        });
    }

    /**
     * Delete saved item
     */
    deleteSavedItem(id) {
        const savedItems = JSON.parse(localStorage.getItem('yougen_saved_items') || '[]');
        const filteredItems = savedItems.filter(item => item.id !== id);
        localStorage.setItem('yougen_saved_items', JSON.stringify(filteredItems));
        
        this.displaySavedItems(filteredItems);
        this.showSuccess('Item deleted!');
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.yougenAI = new YouGenAI();
    window.yougenAI.initializeSavedItems();
});

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = YouGenAI;
} 