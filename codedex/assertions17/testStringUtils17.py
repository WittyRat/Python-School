import unittest
from stringUtils17 import reverse_string, capitalize_string, is_capitalized

class TestStringUtils(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_capitalize_string(self):
        self.assertTrue(capitalize_string("kaRtul"), "Kartul")
    
    def test_is_capitalized(self):
        self.assertTrue(is_capitalized("kana"))

    
    

if __name__ == "__main__":
    unittest.main()
