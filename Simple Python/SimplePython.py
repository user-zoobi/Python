#!/usr/bin/env python
# coding: utf-8

# In[6]:


def greet_user(greeting):
     print(greeting)


# In[7]:


def variable_name(wife_name= "Zelda",husband_name= "Peter"):
    print("The name of the husband and wife are Mr."+ husband_name +" and Mrs."+wife_name)
variable_name()


# In[3]:


def alphabets(winner,score,other_function):
    print("The winner of the game is "+ winner +" team ")
    print("The score made by two team are "+score)
    print("the audience was very "+ other_function)

alphabets("Australian","0-1","energetic")


# In[27]:


# def calculation():
#     y = 1
#     print(y)
#     y = 2
#     whatever(2)
#     print(y)
# calculation()


# In[31]:


def definition_animal(animal_type= "rabbit",describe_animal= "Hazle"):
    print("I have a "+ animal_type + " pet")
    print("And its name is "+ describe_animal )
definition_animal()
    


# In[32]:


def animal_cast(animal_type,define_animal= "Wood"):
    print("My animal name is "+ define_animal )
    print("And it is a "+ animal_type)
animal_cast(animal_type= "cat")


# In[35]:


def describe_pet(animal_type, pet_name):
# """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet("cat","bouce")


# In[43]:


def describe_city(country,city= "Islamabad"):
    print("The capital of "+ country +" is "+city)
describe_city(country="Pakistan")


# In[51]:


def formatted_name(first_name,last_name,middle_name= ''):
    if middle_name:
        full_name = first_name + middle_name + last_name
    else:
        full_name = first_name + last_name
    return full_name
formatted_name("Muhammad"," "," Hassan ")


# In[6]:


class Dog():
    def __init__(self, name , breed):
        self.name = name
        self.breed = breed
        
    def called(self):
        print("The name of my pet is "+ self.name +" dog ")
        
    def type_breed(self):
        message = print("It is a "+ self.breed +"dog")
                        
nick = Dog("Frenchies","German")
print(nick.type_breed())
print(nick.called())

      


# In[1]:


class Car():
    def __init__(self , brand , model,used):
        self.brand = brand
        self.model = model
        self.used = 0
        
    def fnc_01(self):
        print("My car brand is "+ self.brand)
        
    def fnc_02(self):
        print("My car model is of "+ self.model)
        
    def fnc_03(self):
        print("My car used is about "+ self.used)
        
var1 = Car("Toyota",2009,0)
print(var1.fnc_01())
print((var1.fnc_03()))


# In[4]:


class Dog():
    def __init__(self,name,color):
        self.name = name
        self.color = color
    
    def dog_name(self):
        print("My dog name is "+self.name)
    def dog_color(self):
        print("My dog colour is "+ self.color)
        
my_dog = Dog("Scooby","brown")
my_dog2 = Dog("Fred","white")
my_dog.dog_name()
my_dog2.dog_name()


# In[6]:


class Car():
    def __init__(self,car,model,colour,cc,brand):
        self.car = car
        self.model  = model
        self.colour = colour
        self.cc = cc
        self.brand = brand
    
    def car_definition(self):
        print("Car specification "+ self.car +" "+ str(self.model) +" "+ self.colour +" "+ str(self.cc) +" " +self.brand)
        
car_details = Car("Civic",2017,"black",1200,"toyota")
car_details.car_definition()


# In[9]:


class Car():
    def __init__(self,car,model,brand):
        self.car = car
        self.model = model
        self.brand = brand
        self.odometer = 23
        
    def car_definition(self):
        print("Car Details = " + self.car +" "+ str(self.model)+ " " + self.brand)
    def car_odometer(self):
        print("The readind of my car's odometer is "+ str(self.odometer))
        
car_property = Car("mehran",2005,"suzuki")
car_property.car_definition()
car_property.car_odometer()
        


# In[21]:


class Car():
    def __init__(self,car,model,brand):
        self.car = car
        self.model = model
        self.brand = brand
        
    def car_definition(self):
        print("Car Details = " + self.car +" "+ str(self.model)+ " " + self.brand)
    def car_odometer(self,mileage):
        print("The readind of my car's odometer is "+ str(mileage))
        
car_property = Car("mehran",2005,"suzuki")
car_property.car_definition()
car_property.car_odometer(23)
        


# In[19]:


def Car():
    def __init__(self,car,model,brand):
        self.car = car
        self.model = model
        self.brand = brand
        self.odometer = 0
        
    def car_properties(self):
        print("The Car is of "+ self.car + str(self.model) + self.brand )
        
    def odometer(self):
        print("My brand new car has "+ str( self.odometer) +"reading ." )
        
    def change_reading(self,mileage):
        if (mileage > self.odometer):
            self.mileage = mileage
            print("The increased value of reading is "+self.mileage )
            
reading = Car("prado",2018,"suzuki")
reading.car_properties()


# In[11]:


class Car():
        def __init__(self,brand,model,year):
            self.brand = brand
            self.model = model
            self.year = year

        def get_descriptive_name(self):
            print("the car is of"+ self.brand +"model"+str(self.model)+"of year"+self.year)

car1 = Car(1666,"toyota",1999)
print(car1.get_descriptive_name)


# In[3]:


import numpy as np
data = [0,1,2,3,4,5]
data1 = np.array(data)
print(data1)


# In[13]:


import numpy as np
data = ['bob','tom','jess','charles']
data2 = np.array(data)
print(data2 == 'tom')


# In[11]:


import numpy as np

A = np.array([4, 7, 3, 4, 2, 8])

print(A == 4)


# In[1]:


def greetuser():
    print("My name is Zohaib")
greetuser()


# In[15]:


def greetuser(username):
    x =23
    print("Hello! he is " +str(username)+ " and his age is "+str(x) )
greetuser('zohaib')


# In[17]:


def order(order1):
    print("Please take my order of pizza. "+str(order1))
order('pepronni flavour')


# In[18]:


def favourite_book(title):
    print("One of my favourite book is "+str(title))
favourite_book('Alice wonderland')


# In[20]:


def describe_pet(animal_type,pet_name):
    print("my favourite pet is "+ str(animal_type) +" it's name is "+ str(pet_name))
describe_pet('cat','tom')


# In[21]:


def describe_pet(animal_type,pet_name):
    print("my favourite pet is "+ str(animal_type) +" it's name is "+ str(pet_name))
describe_pet('cat','tom')
describe_pet('rat','jerry')


# In[26]:


def my_movie(name_movie,type_movie):
    print("my favourite movie is "+ str(name_movie) +" it is an "+ str(type_movie) +" movie")
my_movie(name_movie='avengers',type_movie='action')


# In[29]:


def movie_base(movie_name,movie_type = 'action'):
    print("The movie name is "+ str(movie_name) +" it is an "+ str(movie_type))
movie_base('avengers')


# In[32]:


def my_name(firstname,middlename,lastname):
    fullname = str(firstname) +" "+ str(middlename) +" "+ str(lastname)
    return fullname.title()
x = my_name('Muhammad','Zohaib','Hassan')
print(x)


# In[3]:


def make_shirt(shirt_type,shirt_size):
    print("The size of the shirt is "+str(shirt_size))
    print("Actually which type of shirt do you want? ")
    print("I want a "+str(shirt_type))
make_shirt('Tshirt',41)


# In[5]:


def describe_city(city_name,city_country = 'Pakistan'):
    print(str(city_name) +" is the city of "+ str(city_country ))
describe_city('Karachi')
describe_city('Naran')
describe_city('Gilgit')


# In[8]:


def get_formatted_name(first_name,last_name):
    fullname = str(first_name)+ " " +str(last_name)
    return fullname
x = get_formatted_name('Muhammad','Zohaib')
print(x)


# In[16]:


def get_formatted_name(firstname,middlename,lastname):
        fullname1 = print('my name is '+ firstname +" "+ middlename +" "+ lastname)
        return fullname1
x = get_formatted_name('Muhammad','','Zohaib')
print(x)za


# In[18]:


def build_person(first_name,last_name):
    fullname = {'first' : first_name ,'second': last_name}
    return fullname
x = build_person('Muhammad','Zohaib')
print(x)


# In[22]:


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


# In[ ]:




