"""Coffee shops are wonderful places to work and study. Like any small business, coffee shops require management to manage inventory, order processing, sales, and menus. Let's use what our knowledge of Python testing to make sure a coffee menu is up to date.

First, set up testing:

Create and save the coffee_menu.py file.
Next, set up a CoffeeMenu class:

In the class set up coffee menu items. It should look like this:
class CoffeeMenu:
  def __init__(self):
    self.menu = {
      'espresso': 2.50,
      'latte': 2.75,
      'cappuccino': 3.20,
      'americano': 2.70
    }

Then, let's define a test class and write some tests:

Create and save the test_coffee_menu.py file with the TestCoffeeMenu class.
Write descriptive unit test using assertions (ex. test_get_price_existing_item(), test_get_price_non_existing_item(), test_add_item())
After running the tests, observe the output to see if all tests pass successfully.

What results did you get? Feel free to share on Twitter!

And once again, happy testing! 🧪"""

class CoffeeMenu:
    def __init__(self):
        self.menu = {
            "espresso": 2.50,
            "latte": 2.75,
            "cappuccino": 3.20,
            "americano": 2.70
        }
    
    def get_price(self, item):
        return self.menu.get(item.lower())

    def add_item(self, item, price):
        self.menu[item.lower()] = price