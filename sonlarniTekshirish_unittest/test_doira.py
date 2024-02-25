import unittest as u
from doira import getArea,getPeremeter

class DoiraTest(u.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(10),314.159)
        self.assertAlmostEqual(getArea(3),28.27431)

    def test_peremeter(self):
        self.assertAlmostEqual(getPeremeter(10),62.8318)
        self.assertAlmostEqual(getPeremeter(4),25.13272)