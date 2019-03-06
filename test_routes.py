import unittest
import app

# Template Render and Route Tests


class TestContainerOnHome(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_container(self):
        rv = self.app.get('/')
        self.assertIn('container', rv.data)

    def test_blogs(self):
        rv = self.app.get('/blogs')
        self.assertIn('Welcome to blogs', rv.data)

    def test_about(self):
        rv = self.app.get('/about')
        self.assertIn('Welcome to About', rv.data)

    def test_homepage(self):
        rv = self.app.get('/home')
        self.assertIn('Welcome to the Homepage', rv.data)

# DB Tests


class DBFunctions(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_container(self):
        rv = self.app.get('/')
        self.assertIn('container', rv.data)

    def test_blogs(self):
        rv = self.app.get('/blogs')
        self.assertIn('Welcome to blogs', rv.data)

    def test_about(self):
        rv = self.app.get('/about')
        self.assertIn('Welcome to About', rv.data)

    def test_homepage(self):
        rv = self.app.get('/home')
        self.assertIn('Welcome to the Homepage', rv.data)
