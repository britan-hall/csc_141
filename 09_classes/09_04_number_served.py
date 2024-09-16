class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f'\nRestaurant: {self.name}')
        print(f'Cuisine Type: {self.cuisine_type}')
        print(f'Customers Served: {self.number_served}')
    
    def open_restaurant(self):
        print(f'{self.name} is now open.')

    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self, increment):
        self.number_served += increment


restaurant = Restaurant('McDonalds','Fast Food')

restaurant.describe_restaurant()

restaurant.set_number_served(1000)
restaurant.describe_restaurant()

restaurant.increment_number_served(100)
restaurant.describe_restaurant()