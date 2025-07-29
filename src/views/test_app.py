import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Create test client
        self.client = app.test_client()
        self.client.testing = True

    def test_homepage_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Create YouTube Content", response.data)

    def test_post_generation_valid_input(self):
        response = self.client.post('/', data={
            'topic': 'AI Tools',
            'tone': 'Informative',
            'audience': 'Students'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'TITLES', response.data)

    def test_missing_topic(self):
        response = self.client.post('/', data={
            'topic': '',
            'tone': 'Casual',
            'audience': 'Creators'
        })
        self.assertIn(b'Please enter a video topic.', response.data)

if __name__ == '__main__':
    unittest.main()
