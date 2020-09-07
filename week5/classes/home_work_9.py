##################### 9-1 ########################
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name= restaurant_name
        self.cuisine_type= cuisine_type
    def describe_restaurant(self):
        print(f"I like {self.cuisine_type} restaurant {self.restaurant_name}.")
    def open_restaurant(self):
        print(f"{self.restaurant_name} will open at 10 a.m.")
my_restaurant= Restaurant("Veselka", 'Ukrainian')
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

###################### 9-2 #########################

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name= restaurant_name
        self.cuisine_type= cuisine_type
    def describe_restaurant(self):
        print(f"I like {self.cuisine_type} restaurant {self.restaurant_name}.")
my_restaurant1= Restaurant("Veselka", 'Ukrainian')
my_restaurant2= Restaurant("Georgia cuisine", 'Georgian')
my_restaurant3= Restaurant("La Shacra", 'Spanish')
my_restaurant1.describe_restaurant()
my_restaurant2.describe_restaurant()
my_restaurant3.describe_restaurant()

################# 9-3 ###############################

class User():
    def __init__(self, first_name, last_name, age):
        self.first_name= first_name.title()
        self.last_name= last_name.title()
        self.age= age
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old.")
    def greet_user(self):
        print(f"Welcome, {self.first_name}, in our company!")
user1= User('nadiya', 'zelman', '36')
user1.describe_user()
user1.greet_user()
user2= User('tatiana', 'shark', '34')
user2.describe_user()
user2.greet_user()
user3= User('polina', 'bond', '30')
user3.describe_user()
user3.greet_user()

######################### 9-4 ##########################
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name= restaurant_name
        self.cuisine_type= cuisine_type
        self.number_served= 0
    def num_customers_served(self):
        print(f"{self.restaurant_name} can serve {str(self.number_served)} customers.")
    def set_number_served(self, number):
        self.number_served=number
    def increment_number_served(self, nums):
        self.number_served += nums

restaurant= Restaurant("Veselka", 'Ukrainian')
restaurant.num_customers_served()

restaurant.number_served= 100
restaurant.num_customers_served()

restaurant.set_number_served(250)
restaurant.num_customers_served()

restaurant.increment_number_served(50)
restaurant.num_customers_served()
