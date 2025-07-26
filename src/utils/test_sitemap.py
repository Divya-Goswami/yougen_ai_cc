#!/usr/bin/env python3
from app import app

def test_sitemap():
    with app.test_client() as client:
        response = client.get('/sitemap.xml')
        print(f"Status Code: {response.status_code}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        print("\nContent Preview:")
        print(response.data.decode()[:500])
        print("\n" + "="*50)
        
        # Check if it's valid XML
        content = response.data.decode()
        if '<?xml version="1.0"' in content and '<urlset' in content:
            print("✅ Valid XML sitemap detected!")
        else:
            print("❌ Invalid XML - might be HTML error page")
            print("Full content:")
            print(content)

if __name__ == "__main__":
    test_sitemap() 