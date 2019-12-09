from unittest import TestCase, main as unittest_main
from app import app
class SoulsTest(TestCase):
    """Flask Tests."""
    def setUp(self):

        self.client = app.test_client()

        app.config['TESTING'] = True

    def test_index(self):
        """Test homepage"""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')

    def test_new(self):
        """Test new"""
        result = self.client.get('/souls/new')
        self.assertEqual(result.status, '200 OK')

    


if __name__ == '__main__':
    unittest_main()
