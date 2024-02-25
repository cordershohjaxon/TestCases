import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_full_name(self):
        formatted_name = get_full_name('alijon','valiyev')
        self.assertEqual(formatted_name,'Alijon Valiyev')
    def test_full_name_fathersname(self):
        formatted_name = get_full_name('hasan','husanov','olimovich')
        self.assertEqual(formatted_name,"Hasan Olimovich Husanov")


