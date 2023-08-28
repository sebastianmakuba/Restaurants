import sys
import os
# Adjust the path to the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from lib.customer import Customer
from lib.restaurant import Restaurant
from lib.review import Review

# Create test instances
customer1 = Customer("Sebastian", "Makuba")
customer2 = Customer("Bill", "Smith")

restaurant1 = Restaurant("Chicken Inn")
restaurant2 = Restaurant("Debonnairs")

# Add reviews
customer1.add_review(restaurant1, 4)
customer2.add_review(restaurant1, 5)

# Test aggregate and association methods
print("Customer 1's full name:", customer1.full_name())
print("Customer 2's family name:", customer2.cust_family_name())

print("All customers:", Customer.all())
print("All restaurants:", Restaurant.all())
print("All reviews:", Review.all())

print("Restaurant 1's reviews:", restaurant1.rest_reviews())
print("Restaurant 1's customers:", restaurant1.rest_customers())

print("Customer 1's num reviews:", customer1.num_reviews())
print("Customer with full name 'Jane Smith':", Customer.find_by_name("Jane Smith"))
print("Customers with given name 'John':", Customer.find_all_by_given_name("John"))

print("Restaurant 1's average star rating:", restaurant1.average_star_rating())
