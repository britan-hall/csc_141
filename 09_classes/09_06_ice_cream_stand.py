class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f'{self.name} is a {self.cuisine_type} restaurant.')

    def open_restaurant(self):
        print(f'{self.name} is now open.')

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ['vanilla','choclate','strawberry']
    
    def display_flavors(self):
        print('Ice Cream Stand flavors:')
        for i in self.flavors:
            print(i)

ice_cream_stand = IceCreamStand('Ice Cream Stand', 'Ice Cream')
ice_cream_stand.display_flavors()

