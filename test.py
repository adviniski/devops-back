import unittest
from api import app

class TestHello(unittest.TestCase):
    
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
    
    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

if __name__ == '__main__':
    unittest.main()