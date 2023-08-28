import unittest
from lib.restaurant import Restaurant

class TestRestaurant(unittest.TestCase):

    def setUp(self):
        self.restaurant = Restaurant("Delicious Eats")

    def test_restaurant_attributes(self):
        self.assertEqual(self.restaurant.name, "Delicious Eats")

    
if __name__ == "__main__":
    unittest.main()
