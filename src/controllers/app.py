from flask import Flask, request, render_template, jsonify, Response, send_from_directory, session
import ollama
import os
import sys
from dotenv import load_dotenv
import re
import time

# Add the config directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'config'))
from config import get_product_config

# Load environment variables
load_dotenv()

# Get the base directory (project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Initialize Flask app with custom template and static folders
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'src', 'views'),
    static_folder=os.path.join(BASE_DIR, 'assets')
)

# Get product configuration
PRODUCT_CONFIG = get_product_config()

# Register a custom Jinja2 filter for regex_replace
@app.template_filter('regex_replace')
def regex_replace(s, find, replace):
    return re.sub(find, replace, s)

# Production configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
app.config['DEMO_MODE'] = os.environ.get('DEMO_MODE', 'False').lower() == 'true'

def clean_and_group_output(output):
    print("DEBUG - Raw AI output:")
    print(output)
    print("=" * 50)

    output = re.sub(r'\*\*([^\*]+)\*\*', r'\1', output)
    output = re.sub(r'\*([^\*]+)\*', r'\1', output)
    output = re.sub(r'^#+\s*', '', output, flags=re.MULTILINE)
    output = re.sub(r'^-\s*', '', output, flags=re.MULTILINE)
    output = re.sub(r'^\*\s*', '', output, flags=re.MULTILINE)
    output = re.sub(r'^•\s*', '', output, flags=re.MULTILINE)
    output = re.sub(r'^\d+\.\s*', '', output, flags=re.MULTILINE)
    output = output.replace('##', '')

    sections = {'titles': [], 'description': [], 'hashtags': [], 'thumbnails': []}
    current = None

    for line in output.split('\n'):
        line = line.strip()
        if not line:
            continue
            
        l = line.lower()
        
        # Skip lines that start with "Thumbnail X:" pattern
        if re.match(r'^thumbnail\s+\d+:', l):
            continue;
        
        if any(h in l for h in ['title suggestion', 'title idea', 'titles:', 'title:', 'titles']):
            current = 'titles'
        elif any(h in l for h in ['description suggestion', 'description idea', 'descriptions:', 'description:', 'descriptions']):
            current = 'description'
        elif any(h in l for h in ['hashtag', 'set', 'tags', 'hashtags']):
            current = 'hashtags'
        elif any(h in l for h in ['thumbnail', 'idea', 'thumbnails']):
            current = 'thumbnails'
        
        if current:
            clean = re.sub(r'^[-*•\d.\s]+', '', line)
        if current == 'description':
            clean = re.sub(r'^(\*\*|__)?description\s*\d+:(\*\*|__)?', '', clean, flags=re.IGNORECASE).strip()
        if clean:
            sections[current].append(clean)

    def ensure_hashtags(groups):
        processed = []
        current_group = []
        for group in groups:
            line = group.replace('*', '').replace('-', '').strip()
            if line.startswith('#'):
                current_group.append(line)
            elif current_group:
                if len(current_group) >= 2:
                    processed.append(' '.join(current_group))
                current_group = []
        if current_group and len(current_group) >= 2:
            processed.append(' '.join(current_group))
        return processed
    if sections['hashtags']:
        sections['hashtags'] = ensure_hashtags(sections['hashtags'])
    # Fallback: if no hashtags, insert default trendy groups
    if not sections['hashtags']:
        sections['hashtags'] = [
            '#YouTube #Viral #Trending #ContentCreator #Subscribe #Explore #Shorts',
            '#Vlog #InstaGood #Like #Share #NewVideo #MustWatch #ViralVideo',
            '#YouTuber #Creator #VideoOfTheDay #FYP #WatchNow #Popular #Discover'
        ]

    print("DEBUG - Sections found:")
    for section_name, content in sections.items():
        print(f"{section_name}: {len(content)} items")
        if content:
            print(f"  Sample: {content[0]}")

    return sections

def safe_ollama_prompt(prompt):
    for _ in range(2):
        try:
            response = ollama.chat(
                model='gemma:2b',
                messages=[{"role": "user", "content": prompt}]
            )
            return response.get('message', {}).get('content', '').strip()
        except Exception:
            time.sleep(1)
    return ""

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    error = None
    sections = None

    # Only apply limit if in demo mode
    if app.config['DEMO_MODE']:
        if 'generation_count' not in session:
            session['generation_count'] = 0

    if request.method == 'POST':
        if app.config['DEMO_MODE'] and session.get('generation_count', 0) >= 5:
            error = "Demo limit reached. Please purchase the full version to unlock unlimited generations."
        else:
            try:
                topic = request.form.get('topic', '').strip()
                tone = request.form.get('tone', '').strip()
                audience = request.form.get('audience', '').strip()

                if not topic:
                    error = "Please enter a video topic."
                elif not tone:
                    error = "Please select a content tone."
                elif not audience:
                    error = "Please select a target audience."
                else:
                    titles_prompt = f"should be give 5 YouTube titles for '{topic}' in a '{tone}' tone for '{audience}' audience."
                    desc_prompt = f"should be Give 3 short YouTube descriptions (minimum character limit: 250) for '{topic}' in '{tone}' tone."
                    tags_prompt = (
                        f"Give minimum exactly 3 groups of 5-7 highly relevant, trendy hashtags for a YouTube video about '{topic}' in a '{tone}' tone. "
                        "Each group should be a single line, space-separated, with each hashtag starting with #. "
                        "Do not include any explanations, group labels, or bullets. Only output the hashtags, like this:\n"
                        "#tag1 #tag2 #tag3 #tag4 #tag5\n"
                        "#tag6 #tag7 #tag8 #tag9 #tag10\n"
                        "#tag11 #tag12 #tag13 #tag14 #tag15"
                    )
                    thumb_prompt = f"should be give minimum 3 thumbnail ideas for '{topic}' in '{tone}' tone."

                    titles = safe_ollama_prompt(titles_prompt)
                    descs = safe_ollama_prompt(desc_prompt)
                    tags = safe_ollama_prompt(tags_prompt)
                    thumbs = safe_ollama_prompt(thumb_prompt)

                    raw_output = f"""
TITLES:
{titles}

DESCRIPTIONS:
{descs}

HASHTAGS:
{tags}

THUMBNAIL IDEAS:
{thumbs}
"""
                    print("DEBUG - Ollama raw response:", raw_output)
                    output = raw_output
                    sections = clean_and_group_output(output)
                    # Increment generation count only in demo mode
                    if app.config['DEMO_MODE']:
                        session['generation_count'] += 1
            except Exception as e:
                error = f"Error generating content: {str(e)}"
                app.logger.error(f"Content generation error: {e}")

    return render_template('index.html', output=output, error=error, sections=sections, config=PRODUCT_CONFIG)

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "service": "YouGen: AI YouTube Content Generator"})

@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    import datetime
    import os
    try:
        # Only include real, existing pages
        pages = [
            {'loc': request.url_root.rstrip('/') + '/', 'priority': '1.0', 'changefreq': 'weekly'},
            {'loc': request.url_root.rstrip('/') + '/blog', 'priority': '0.8', 'changefreq': 'monthly'},
        ]
        lastmod = datetime.date.today().isoformat()
        xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        for page in pages:
            xml.append('  <url>')
            xml.append(f'    <loc>{page["loc"]}</loc>')
            xml.append(f'    <lastmod>{lastmod}</lastmod>')
            xml.append(f'    <changefreq>{page["changefreq"]}</changefreq>')
            xml.append(f'    <priority>{page["priority"]}</priority>')
            xml.append('  </url>')
        xml.append('</urlset>')
        xml_content = '\n'.join(xml)
        return Response(xml_content, mimetype='application/xml', headers={'Content-Type': 'application/xml; charset=utf-8'})
    except Exception as e:
        app.logger.error(f"Sitemap generation error: {e}")
        # Fallback to static sitemap if dynamic generation fails
        static_path = os.path.join(app.root_path, 'static', 'sitemap.xml')
        if os.path.exists(static_path):
            with open(static_path, 'r') as f:
                return Response(f.read(), mimetype='application/xml', headers={'Content-Type': 'application/xml; charset=utf-8'})
        # Final fallback - minimal valid sitemap
        xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://tubegenuis.online/</loc>
    <lastmod>2025-01-01</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>'''
        return Response(xml_content, mimetype='application/xml', headers={'Content-Type': 'application/xml; charset=utf-8'})

# Blog posts data
BLOG_POSTS = {
    'ai-changing-youtube': {
        'title': 'How AI is Changing YouTube Content Creation',
        'date': 'March 21, 2025',
        'read_time': 5,
        'image': '/assets/images/blog/ai-youtube.jpg',
        'content': '''
            <p>Artificial Intelligence is revolutionizing how creators approach YouTube content creation. From generating engaging titles to crafting compelling descriptions, AI tools are becoming indispensable for content creators looking to stay ahead in the competitive world of video content.</p>

            <h2>The Rise of AI in Content Creation</h2>
            <p>As we move further into 2025, AI tools are becoming increasingly sophisticated, offering creators unprecedented capabilities in content generation and optimization. Here's how AI is transforming different aspects of YouTube content creation:</p>

            <h3>1. Title Generation</h3>
            <p>AI algorithms can now analyze millions of successful YouTube titles to generate options that are both engaging and SEO-optimized. This helps creators save time while ensuring their videos have the best chance of being discovered.</p>

            <h3>2. Description Optimization</h3>
            <p>AI tools can generate detailed, keyword-rich descriptions that help videos rank better in search results while maintaining natural readability and engagement.</p>

            <h3>3. Thumbnail Creation</h3>
            <p>AI-powered tools can now suggest thumbnail designs based on what performs best in your niche, taking into account elements like color schemes, text placement, and image composition.</p>

            <h2>Practical Applications</h2>
            <p>Here are some ways creators are using AI to enhance their content:</p>
            <ul>
                <li>Generating multiple title variations for A/B testing</li>
                <li>Creating timestamped descriptions automatically</li>
                <li>Suggesting trending hashtags for better reach</li>
                <li>Optimizing thumbnails for different devices</li>
            </ul>

            <h2>The Future of AI in YouTube Content</h2>
            <p>As AI technology continues to evolve, we can expect even more innovative tools and features to emerge. The key for creators will be learning how to effectively integrate these tools into their workflow while maintaining their unique voice and style.</p>
        ''',
        'tags': ['AI', 'YouTube', 'Content Creation', 'Digital Marketing'],
        'author': 'Sarah Johnson',
        'author_image': '/static/authors/sarah.jpg',
        'author_bio': 'Digital Marketing Specialist & Content Creator',
        'related_posts': [
            {
                'url': '/blog/viral-youtube-titles',
                'title': '5 Tips for Viral YouTube Titles',
                'excerpt': 'Learn the secrets to crafting irresistible YouTube titles that drive clicks and boost your channel\'s growth.',
                'image': '/assets/images/blog/viral-titles.jpg'
            },
            {
                'url': '/blog/optimizing-thumbnails-ai',
                'title': 'Optimizing Thumbnails with AI',
                'excerpt': 'See how AI tools can help you design eye-catching thumbnails that increase your video views and engagement.',
                'image': '/assets/images/blog/thumbnails.jpg'
            }
        ]
    },
    'viral-youtube-titles': {
        'title': '5 Tips for Viral YouTube Titles',
        'date': 'March 19, 2025',
        'read_time': 4,
        'image': '/assets/images/blog/viral-titles.jpg',
        'content': '''
            <p>Creating viral YouTube titles is both an art and a science. In this guide, we'll explore five proven strategies that can help your videos get more clicks and views.</p>

            <h2>Why Titles Matter</h2>
            <p>Your video title is the first thing potential viewers see. It's your chance to make a strong impression and convince them to click. Here are our top tips for crafting viral titles:</p>

            <h3>1. Use Numbers and Lists</h3>
            <p>Titles with numbers tend to perform better as they set clear expectations for viewers. For example: "5 Proven Ways to Grow Your Channel" or "10 YouTube Tips Nobody Tells You".</p>

            <h3>2. Include Emotional Triggers</h3>
            <p>Words that evoke emotion can significantly increase click-through rates. Terms like "amazing," "shocking," or "unbelievable" can be effective when used authentically.</p>

            <h3>3. Optimize for Search</h3>
            <p>Include relevant keywords in your titles while keeping them natural and engaging. Use tools like YouGen AI to find the perfect balance between SEO and appeal.</p>

            <h3>4. Create Curiosity</h3>
            <p>Craft titles that make viewers curious enough to click, but avoid clickbait that doesn't deliver on its promise.</p>

            <h3>5. Keep It Concise</h3>
            <p>The ideal title length is 60-70 characters. This ensures your full title is visible in search results and suggested videos.</p>

            <h2>Real-World Examples</h2>
            <p>Here are some examples of titles that have proven to be successful:</p>
            <ul>
                <li>"How I Gained 100K Subscribers in 30 Days (Proven Strategy)"</li>
                <li>"5 YouTube Secrets That Changed My Life"</li>
                <li>"The One Thing Successful YouTubers Never Tell You"</li>
            </ul>
        ''',
        'tags': ['YouTube Tips', 'Content Strategy', 'Video Marketing'],
        'author': 'Mike Chen',
        'author_image': '/static/authors/mike.jpg',
        'author_bio': 'YouTube Growth Strategist',
        'related_posts': [
            {
                'url': '/blog/ai-changing-youtube',
                'title': 'How AI is Changing YouTube Content Creation',
                'excerpt': 'Discover how artificial intelligence is revolutionizing the way creators generate ideas, titles, and thumbnails.',
                'image': '/assets/images/blog/ai-youtube.jpg'
            },
            {
                'url': '/blog/optimizing-thumbnails-ai',
                'title': 'Optimizing Thumbnails with AI',
                'excerpt': 'See how AI tools can help you design eye-catching thumbnails that increase your video views and engagement.',
                'image': '/assets/images/blog/thumbnails.jpg'
            }
        ]
    },
    'optimizing-thumbnails-ai': {
        'title': 'Optimizing Thumbnails with AI',
        'date': 'March 17, 2025',
        'read_time': 6,
        'image': '/assets/images/blog/thumbnails.jpg',
        'content': '''
            <p>Thumbnails are crucial for YouTube success. With AI tools, creating eye-catching thumbnails has become easier and more effective than ever. Here's your complete guide to optimizing thumbnails using AI.</p>

            <h2>The Power of AI in Thumbnail Creation</h2>
            <p>AI-powered tools can analyze millions of successful thumbnails to identify patterns and elements that drive clicks. Here's how to leverage this technology:</p>

            <h3>1. Color Selection</h3>
            <p>AI can suggest color combinations that catch viewers' attention while maintaining brand consistency. Learn how to use these suggestions effectively.</p>

            <h3>2. Text Placement</h3>
            <p>Discover how AI analyzes viewing patterns to recommend optimal text placement for maximum impact.</p>

            <h3>3. Image Composition</h3>
            <p>Use AI to identify the most effective ways to compose your thumbnail images for different types of content.</p>

            <h2>Step-by-Step Guide</h2>
            <ol>
                <li>Start with a clear, high-quality base image</li>
                <li>Use AI to analyze and optimize the composition</li>
                <li>Add text and graphics based on AI recommendations</li>
                <li>Test different variations with A/B testing</li>
            </ol>

            <h2>Best Practices</h2>
            <p>Even with AI assistance, keep these fundamental principles in mind:</p>
            <ul>
                <li>Maintain consistency with your brand</li>
                <li>Ensure text is readable on all devices</li>
                <li>Use contrasting colors for better visibility</li>
                <li>Keep designs clean and uncluttered</li>
            </ul>
        ''',
        'tags': ['Thumbnails', 'YouTube SEO', 'AI Tools', 'Design'],
        'author': 'Lisa Wong',
        'author_image': '/static/authors/lisa.jpg',
        'author_bio': 'AI & Design Expert',
        'related_posts': [
            {
                'url': '/blog/ai-changing-youtube',
                'title': 'How AI is Changing YouTube Content Creation',
                'excerpt': 'Discover how artificial intelligence is revolutionizing the way creators generate ideas, titles, and thumbnails.',
                'image': '/assets/images/blog/ai-youtube.jpg'
            },
            {
                'url': '/blog/viral-youtube-titles',
                'title': '5 Tips for Viral YouTube Titles',
                'excerpt': 'Learn the secrets to crafting irresistible YouTube titles that drive clicks and boost your channel\'s growth.',
                'image': '/assets/images/blog/viral-titles.jpg'
            }
        ]
    }
}

@app.route('/blog/<slug>')
def blog_post(slug):
    post = BLOG_POSTS.get(slug)
    if not post:
        return render_template('404.html'), 404
    return render_template('blog_post.html', post=post, related_posts=post.get('related_posts', []))

@app.route('/blog')
def blog():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Top 10 AI Tools for YouTubers in 2025 (Including the Secret Weapon: YouGen AI)</title>
      <meta name="description" content="Discover the top 10 AI tools for YouTubers in 2025, including YouGen AI—the all-in-one AI YouTube content generator for titles, descriptions, hashtags, and thumbnails.">
      <meta name="keywords" content="AI YouTube tools, YouGen AI, YouTube content generator, AI for YouTubers, YouTube SEO, AI video editing, AI scriptwriting, YouTube thumbnail AI, YouTube growth tools, 2025 YouTube AI">
      <link rel="canonical" href="https://tubegenuis.online/blog" />
      <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
      <style>
        body { font-family: 'Inter', Arial, sans-serif; background: #f8fafc; color: #222; margin: 0; padding: 0; }
        .blog-container { max-width: 820px; margin: 48px auto; background: #fff; padding: 48px 32px 40px 32px; border-radius: 18px; box-shadow: 0 8px 32px rgba(44,62,80,0.10); }
        h1 { font-size: 2.5rem; font-weight: 700; color: #d32f2f; margin-bottom: 0.5em; }
        h2 { font-size: 1.6rem; color: #b71c1c; margin-top: 2.5em; margin-bottom: 0.7em; font-weight: 700; }
        h3 { font-size: 1.2rem; color: #d32f2f; margin-top: 2em; margin-bottom: 0.5em; font-weight: 600; }
        p { font-size: 1.08rem; line-height: 1.8; margin-bottom: 1.3em; }
        ol { padding-left: 1.3em; margin-bottom: 2em; }
        li { margin-bottom: 1.7em; }
        .tool-title { font-weight: 700; color: #b71c1c; font-size: 1.13rem; }
        .highlight { background: #fff3cd; padding: 2px 8px; border-radius: 4px; font-weight: 600; }
        a { color: #1976d2; text-decoration: underline; }
        .cta-section { background: linear-gradient(90deg, #ff5252 0%, #ffb300 100%); color: #fff; border-radius: 14px; padding: 32px 28px; margin: 40px 0 0 0; text-align: center; box-shadow: 0 4px 24px rgba(255, 82, 82, 0.08); }
        .cta-section h2 { color: #fff; margin-bottom: 0.5em; }
        .cta-btn { display: inline-block; background: #fff; color: #d32f2f; font-weight: 700; font-size: 1.1rem; padding: 14px 36px; border-radius: 8px; margin-top: 18px; text-decoration: none; box-shadow: 0 2px 8px rgba(44,62,80,0.10); transition: background 0.2s, color 0.2s; }
        .cta-btn:hover { background: #ffe082; color: #b71c1c; }
        @media (max-width: 600px) {
          .blog-container { padding: 18px 6vw 24px 6vw; }
          h1 { font-size: 2rem; }
        }
      </style>
    </head>
    <body>
      <div class="blog-container">
        <h1>Top 10 AI Tools for YouTubers in 2025 <span style="font-size:1.2rem; color:#444;">(Including the Secret Weapon: YouGen AI)</span></h1>
        <p>Are you a YouTuber looking to grow faster, rank higher, and publish smarter in 2025? AI is transforming how content creators operate—from writing scripts to designing thumbnails and crafting perfect titles. In this post, we'll share the <strong>top 10 AI tools for YouTubers in 2025</strong>—including the breakthrough tool everyone's talking about: <span class="highlight">YouGen AI</span>.</p>
        <ol>
          <li><span class="tool-title">YouGen AI – AI YouTube Content Generator</span><br>
            <span style="color:#333;">Best for:</span> Title, Description, Hashtag, and Thumbnail idea generation.<br>
            YouGen AI is an all-in-one AI-powered content generator that helps creators craft high-converting YouTube content in seconds. Just enter your topic, tone, and audience—and boom! Get 3–5 title options, SEO-optimized descriptions, hashtags, and thumbnail suggestions.<br>
            <span style="color:#333;">Perfect for:</span> YouTubers, marketers, freelancers<br>
            Website: <a href="https://tubegenuis.online" target="_blank" rel="noopener">https://tubegenuis.online</a>
          </li>
          <li><span class="tool-title">Descript</span><br>
            <span style="color:#333;">AI for editing video & podcast content.</span> Turn your voice or video into editable text. Delete "ums" with one click. Amazing for content creators who want fast editing.
          </li>
          <li><span class="tool-title">Copy.ai</span><br>
            <span style="color:#333;">Scriptwriting for intros, hooks, and storytelling.</span> Whether you're a vlogger or educator, Copy.ai helps generate engaging scripts based on your keywords or video ideas.
          </li>
          <li><span class="tool-title">Canva Magic Studio</span><br>
            <span style="color:#333;">AI-powered thumbnail and video post design.</span> Get thumbnail ideas, text overlays, and templates all tailored for YouTube's design standards.
          </li>
          <li><span class="tool-title">VidIQ</span><br>
            <span style="color:#333;">YouTube growth analytics & keyword tools.</span> Used by top creators to find trending topics, competitor stats, and keyword opportunities.
          </li>
          <li><span class="tool-title">Pictory</span><br>
            <span style="color:#333;">Turn blog posts or long text into YouTube videos.</span> Great for content repurposing and automating video generation from written material.
          </li>
          <li><span class="tool-title">Lumen5</span><br>
            <span style="color:#333;">AI video creation from text and templates.</span> If you need social-ready videos for YouTube Shorts or Reels, this one's fast and beginner-friendly.
          </li>
          <li><span class="tool-title">ChatGPT + Prompt Templates</span><br>
            <span style="color:#333;">Use prompts to generate scripts, ideas, titles, and community posts.</span> It's flexible and powerful—especially if you know how to prompt it right.
          </li>
          <li><span class="tool-title">RunwayML</span><br>
            <span style="color:#333;">AI video effects, face blur, background removal.</span> A must for creators looking to produce cinematic content without a big budget.
          </li>
          <li><span class="tool-title">Rev.com or Whisper AI</span><br>
            <span style="color:#333;">AI subtitle generation and voice-to-text.</span> Captions increase watch time. These tools let you add accurate subs in minutes.
          </li>
        </ol>
        <h2>Final Thoughts: Why YouGen AI Is the AI Tool to Watch in 2025</h2>
        <p>While most AI tools focus on one task, <span class="highlight">YouGen AI</span> offers a complete YouTube content kit—titles, descriptions, tags, and thumbnail ideas—at once. Whether you're just starting your channel or scaling an agency, it will save hours and boost your results.</p>
        <div class="cta-section">
          <h2>Ready to Supercharge Your YouTube Channel?</h2>
          <p>Try YouGen AI now and experience the AI-powered difference for yourself.</p>
          <a class="cta-btn" href="https://tubegenuis.online" target="_blank" rel="noopener">Try YouGen AI Free</a>
        </div>
      </div>
    </body>
    </html>
    '''

@app.route('/documentation')
def documentation():
    docs_path = os.path.join(os.getcwd(), 'docs')
    return send_from_directory(docs_path, 'DOCUMENTATION.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG'])
