import unittest
from lib.customer import Customer
from lib.restaurant import Restaurant
from lib.review import Review

class TestReview(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("John", "Doe")
        self.restaurant = Restaurant("Delicious Eats")
        self.review = Review(self.customer, self.restaurant, 4)

    def test_review_attributes(self):
        self.assertEqual(self.review.rating, 4)

    

if __name__ == "__main__":
    unittest.main()
