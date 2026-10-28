"""
Test cases for Service Routes
"""
import unittest
from service import app


class TestRoutes(unittest.TestCase):
    """Test Cases for Service Routes"""

    def setUp(self):
        self.client = app.test_client()

    def test_health(self):
        """It should return healthy status"""
        resp = self.client.get("/health")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data["message"], "OK")

    def test_index(self):
        """It should return service info"""
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn("name", data)


if __name__ == "__main__":
    unittest.main()
