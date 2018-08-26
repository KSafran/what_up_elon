import unittest
import app

class RoutesTest(unittest.TestCase):
    """Tests for routes"""

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_answer_string_route(self):
        index = self.app.get('/')
        assert index.status_code == 200

