

class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def dog_name(self):
        print('my dog name is '+str(self.name))
        
    def dog_age(self):
        print('my dog age is '+str(self.age))
        
dog1 = Dog('tom',23)
dog1.dog_name()
dog1.dog_age()


# In[1]:


import tensorflow as tf
tf.__version__


# In[3]:


class Dog():
    def __init__(self,name,creed):
        self.name = name
        self.creed = creed
    
    def dog_name(self):
        print("My dog name is "+ self.name)
        print(self.name +" is a very nice dog")
        
    def dog_creed(self):
        print("My dog cast is "+ self.creed)
        print(self.creed +" they are very unique dogs ")
        
animal = Dog('tom','roadkiller')
animal.dog


# In[1]:


class Dog():
    
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
        
    def dog_name(self):
        print("my dog is "+ self.name)
        
    def dog_type(self):
        print("my dog type is "+ self.breed)
        
dog1 = Dog('tom','roadkiller')
dog1.dog_name()
dog1.dog_type()


# Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating
# that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.

# In[5]:


class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print("The name of the restaurant is "+ self.restaurant_name)
        
    def open_restaurant(self):
        print("The restaurant containing item like "+ self.cuisine_type)
              
place = Restaurant('Pizzahut','Pizza')
place1 = Restaurant('PizzaHut','Curry')

place.describe_restaurant()
place1.open_restaurant()
place.open_restaurant()


# In[6]:


class User():
        def __init__(self,make,model,year):
            self.make = make
            self.model = model
            self.year = year
        
        def manufacture(self):
            print("The car is manufactured in "+ str(self.make))
        
        def car_model(self):
            print("The model of the car is "+ str(self.model))
            
        def car_year(self):
            print("The car is made in "+ str(self.year))
            
user = User('Toyota',2016,2000)
user.manufacture()
user.car_model()
user.car_year()


# In[7]:


class User():
        def __init__(self,make,model,year):
            self.make = make
            self.model = model
            self.year = year
            self.odometer = 0
        
        def car_model(self):
            print("This car belonged to the year of "+ str(self.model))
            
        def car_odometer(self):
            
            print("the reading of odometer is almost "+ str(self.odometer))
            
user = User('Toyota','2007','2006')
user.car_model()
user.car_odometer()


# QNO : 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating
# that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.

# QNO : 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

# In[13]:


class Restaurant():
    def __init__(self,restaurant_name,cuisine_type,number_served ):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
        
    def describe_restaurant(self):
        print("The name of the restaurant is "+ self.restaurant_name)
        
    def open_restaurant(self):
        print("The restaurant containing item like "+ self.cuisine_type)
        
    def set_number_served(self, guest = '0'):
        guest = self.number_served
        print("The total customer served are " + str(guest))
    
place = Restaurant('Pizzahut','Pizza',0)
place.describe_restaurant()
place.open_restaurant()
place.set_number_saved()


# In[ ]:




