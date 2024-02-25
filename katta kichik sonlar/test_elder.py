import unittest
from katta_kichik import find_elder

class TestKattaKichik(unittest.TestCase):
    def test_find_elder(self):
        elder_one = find_elder(2, 5, 8)
        self.assertEqual(elder_one, 8)
