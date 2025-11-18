from coffeMenu20 import CoffeeMenu
import unittest

class TestCoffeeMenu(unittest.TestCase):

    def setUp(self):
        self.menu = CoffeeMenu()

    def tearDown(self):
        self.menu = None
    
    def test_get_price_existing_item(self):
        self.assertEqual(self.menu.get_price("americano"), 2.70)

    def test_get_price_non_existing_item(self):
        self.assertIsNone(self.menu.get_price("milk"))
        
    def test_add_item(self):
        self.menu.add_item("milk", 1.30)
        self.assertEqual(self.menu.get_price("milk"), 1.30)

if __name__ == "__main__":
    unittest.main()
