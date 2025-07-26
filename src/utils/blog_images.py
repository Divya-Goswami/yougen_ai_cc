from PIL import Image, ImageDraw, ImageFont
import os

def create_blog_image(filename, title, size=(800, 400)):
    # Create a new image with a gradient background
    image = Image.new('RGB', size, color='#00BCD4')
    draw = ImageDraw.Draw(image)
    
    # Add some styling
    draw.rectangle([0, 0, size[0], size[1]], fill='#00BCD4')
    draw.rectangle([20, 20, size[0]-20, size[1]-20], outline='#FFFFFF', width=2)
    
    # Add title text
    try:
        font = ImageFont.truetype("Arial", 40)
    except:
        font = ImageFont.load_default()
    
    # Center the text
    text_width = draw.textlength(title, font=font)
    text_x = (size[0] - text_width) // 2
    text_y = (size[1] - 40) // 2
    
    # Draw text with a slight shadow effect
    draw.text((text_x+2, text_y+2), title, font=font, fill='#000000')
    draw.text((text_x, text_y), title, font=font, fill='#FFFFFF')
    
    # Save the image
    image.save(f'static/blog-images/{filename}')

def create_author_avatar(filename, initials, size=(200, 200)):
    # Create a new image with a solid background
    image = Image.new('RGB', size, color='#4CAF50')
    draw = ImageDraw.Draw(image)
    
    # Add initials
    try:
        font = ImageFont.truetype("Arial", 80)
    except:
        font = ImageFont.load_default()
    
    # Center the text
    text_width = draw.textlength(initials, font=font)
    text_x = (size[0] - text_width) // 2
    text_y = (size[1] - 80) // 2
    
    # Draw text
    draw.text((text_x, text_y), initials, font=font, fill='#FFFFFF')
    
    # Save the image
    image.save(f'static/authors/{filename}')

if __name__ == "__main__":
    # Create blog post images
    create_blog_image('ai-youtube.jpg', 'AI in YouTube')
    create_blog_image('viral-titles.jpg', 'Viral Titles')
    create_blog_image('thumbnails.jpg', 'Thumbnail Design')
    
    # # Create author avatars
    # create_author_avatar('sarah.jpg', 'SJ')
    # create_author_avatar('mike.jpg', 'MC')
    # create_author_avatar('lisa.jpg', 'LW')
    
    print("Images created successfully!") 