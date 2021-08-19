"""9-1"""
class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("Restaurant is open")

restaurant=Restaurant('canguan','jin')
print(restaurant.restaurant_name+' ' +restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

