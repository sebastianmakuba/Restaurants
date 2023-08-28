import unittest
from lib.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("John", "Doe")

    def test_customer_attributes(self):
        self.assertEqual(self.customer.given_name, "John")
        self.assertEqual(self.customer.family_name, "Doe")

    def test_customer_full_name(self):
        self.assertEqual(self.customer.full_name(), "John Doe")

    

if __name__ == "__main__":
    unittest.main()
