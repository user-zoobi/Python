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





# In[3]:

