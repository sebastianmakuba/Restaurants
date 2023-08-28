import unittest
from lib.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Sebastian", "Makuba")

    def test_customer_attributes(self):
        self.assertEqual(self.customer.given_name, "Sebastian")
        self.assertEqual(self.customer.family_name, "Makuba")

    def test_customer_full_name(self):
        self.assertEqual(self.customer.full_name(), "Sebastian Makuba")

    

if __name__ == "__main__":
    unittest.main()
