class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self.name

    @classmethod
    def all(cls):
        return cls.all_restaurants

    def add_review(self, review):
        self.reviews.append(review)

    def rest_reviews(self):
        return self.reviews

    def rest_customers(self):
        unique_customers = set()
        for review in self.reviews:
            unique_customers.add(review.customer)
        return list(unique_customers)

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_rating = sum(review.rating for review in self.reviews)
        return total_rating / len(self.reviews)
