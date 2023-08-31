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


print('All Customers:')
for customer in Customer.all():
    print(customer.full_name())

# print("All restaurants:", Restaurant.all())
print("\nAll restaurants:")
for restaurant in Restaurant.all():
    print(restaurant.name)

# print("All reviews:", Review.all())
print("\nAll reviews:")
for review in Review.all():
    print(f"Customer: {review.customer.full_name()}, Restaurant: {review.restaurant.name}, Rating: {review.rating}")

# print("Restaurant 1's reviews:", restaurant1.rest_reviews())
print("\nRestaurant 1's reviews:")
for review in restaurant1.reviews:
    print(f"Customer: {review.customer.full_name()}, Rating: {review.rating}")
# print("Restaurant 1's customers:", restaurant1.rest_customers())
print("\nRestaurant 1's customers:")
for customer in restaurant1.rest_customers():
    print(customer.full_name())

print("Customer 1's num reviews:", customer1.num_reviews())
# print("Customer with full name 'Sebastian Makuba':", Customer.find_by_name("Sebastian Makuba"))
print("\nCustomer with full name 'Sebastian Makuba':")
fullname = Customer.find_by_name("Sebastian Makuba")
if fullname:
    print(fullname.full_name())
else:
    print("Customer not found")

print("\nCustomers with given name 'Sebastian':")
search_fullname = Customer.find_all_by_given_name("Sebastian")
for customer in search_fullname:
    print(customer.full_name())
# print("Customers with given name 'Sebastian':", Customer.find_all_by_given_name("Sebastian"))

print("Restaurant 1's average star rating:", restaurant1.average_star_rating())
