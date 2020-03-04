#!/usr/bin/env python
# coding: utf-8

# In[3]:


def greet_user(username):
    print('Her name is '+username)
greet_user('Anusha')


# In[5]:


def display_message(name):
    print('Hello sir how are you '+name)
display_message('Iftikhar')


# In[6]:


def describe_pet(animal_type, pet_name):
    print("the animal is "+animal_type)
    print("the name of the pet is "+pet_name)
describe_pet('cat','tommy')


# In[8]:


def describe_pet(animal_type,animal_name):
    print('the name of the animal is '+animal_type)
    print('the nickname of the pet is'+animal_name)
describe_pet(animal_type = 'cat', animal_name = 'tom')


# In[2]:


def make_shirt(shirt_size,shirt_message):
    print('The size of the shirt is '+str(shirt_size))
    print('The poster on shirt is '+shirt_message)
make_shirt(36,'hello')


# In[3]:


def get_formatted_name(first_name, last_name):
    full_name = first_name +' '+ last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# In[2]:


def get_formatted_name(first_name, middle_name, last_name):
    full_name = first_name +" "+middle_name+" "+last_name
    return full_name
musician = get_formatted_name('john','lee','hooker')
print(musician)


# In[1]:


pip install scipy


# In[3]:


import numpy as np
from scipy import sparse
eye =np.eye(4)
print('Numpy array:\n{}'.format(eye))


# In[5]:


arr = np.array([[1,2,3],[4,5,6]])
arr
arr*arr


# In[4]:


import numpy as np
arr = np.arange(10)
arr
arr[5]
arr[5:8]


# In[11]:


import numpy as np
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d


# In[14]:


arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[0,1,1]]])
arr3d


# In[15]:


arr3d[1][0]


# In[17]:


arr3d[1][1:6]


# In[38]:


import numpy as np
names = np.array(['Bob','Joe','Will','Smith','Sam','Bill','Garry'])
data = np.random.randn(7,4)


# In[39]:


names


# In[40]:


data


# In[42]:


cond = names == 'Bob'
data[~cond]


# In[43]:


mask = (names == 'Bob') | (names == 'Will')
mask


# In[46]:


arr23 = np.arange(15).reshape((3,5))
arr23


# In[47]:


arr.T


# In[48]:


arr = np.random.randn(6,3)
arr


# In[49]:


np.dot(arr.T,arr)


# In[50]:


arr = np.random.randn(16).reshape((2,2,4))
arr


# In[51]:


arr.transpose((1,0,2))


# In[52]:


x = np.random.randn(8)
x


# In[54]:


from PIL import Image
import numpy as np

im = np.array(Image.open('Owais.jpeg'))

print(im.dtype)


# In[55]:


print(im.shape)


# In[1]:


import pandas as pd
obj = pd.Series([1,2,3,4])
obj


# In[2]:


obj2 = pd.Series([4,7,-5,3] , index =['a','b','c','d'])
obj2


# In[8]:


sdata = {'Ohio':35000, 'Texas':12000, 'Oregon':16000, 'Utah':5000}
obj3 = pd.Series(sdata)
obj3


# In[10]:


states = ['Ohio','Texas','Oregon','Utah']
obj4 = pd.Series(sdata, index=states)
obj4


# In[9]:


import numpy as np
arr = np.arange(10)
arr
arr3 = np.sqrt(arr)
arr3
np.maximum(arr,arr3)


# In[10]:


arr = np.random.randn(5,4)
arr


# In[5]:


import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
arr

arr2 = np.array([[0,4,1],[7,2,12]])
arr2

arr > arr2


# In[17]:


arr = np.arange(10)
arr
arr[5]
arr[5:8]
arr[5:8] = 12
arr

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d
arr2d[2]
arr2d[1,2]


# In[23]:


arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[0,1,0]]])
arr3d
arr3d[0]


# In[27]:


names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
data = np.random.randn(7,4)
names
data
data[names == 'Bob',2:]
names != 'Bob'


# In[30]:


arr = np.empty((8,4))
for  i in range(8):
    arr[i] = i
arr


# In[3]:


import numpy as np
arr = np.arange(15).reshape((3,5))
arr
arr.T


# In[5]:


arr = np.random.randn(6,3)
arr
np.dot(arr.T, arr)


# In[5]:


import numpy as np
names = np.array(['Bob','Will','Mary','Jane','Simon','Clarke'])
names
numbers = np.random.randn(4,4)
numbers
names == 'Bob'


# In[17]:


arr = np.empty((7,4))
for i in range(7):
    arr[i] = i
arr
arr[[4,3,0,6,0,6,0,0]]
arr3 = np.random.randn(6,3)
arr3
np.dot(arr3.T,arr3)


# In[2]:


import pandas as pd
obj = pd.Series([4,7,5,3])
obj


# In[4]:


import pandas as pd
from pandas import Series
sdata = ['Ohio':2500,'California':1500,'Karachi':1500]
sdata3 = Series(sdata)
sdata3


# In[1]:


import pandas as pd
obj2 = pd.Series([4,7,-5,3], index=['d','b','a','c'])
obj2


# In[12]:


sdata = {'Ohio': 35000, 'Califronia': 71000, 'Texas': 16000, 'Oregon': 5000}
obj3 = pd.Series(sdata)
obj3
states = ['Ohio','California','Texas','Oreo']
obj4 = pd.Series(sdata, index = states)
obj4
pd.isnull(obj4)
obj3 + obj4
obj4.name = 'population'
obj4.index.name = 'state'
obj4
obj4.index = ['Bob','Steve','Finn','Hasting']
obj4


# In[4]:


import pandas as pd
sdata = {'Ohio':3500, 'Texas':71000, 'Oregon':16000, 'Utah':5000}
states = ['California','Ohio','Oregon','Texas']
obj4 = pd.Series(sdata, index=states)
obj4


# In[5]:


pd.isnull(obj4)


# In[12]:


import pandas as pd
obj = pd.Series([4,7,-5,3])
obj


# In[5]:


sdata = {'ohio':35000, 'Texas':71000, 'Oregon':16000, 'Utah':5000}
obj3 = pd.Series(sdata)
obj3


# In[6]:


import pandas as pd
states = ['California','Ohio','Oregon','Texas']
obj4 = pd.Series(sdata, index= states)
obj4


# In[10]:


obj3
obj4
obj4.name = 'popuation'
obj4


# In[13]:


obj.index = ['Bob','steve','jeff','ryan']
obj


# In[17]:


from pandas import DataFrame
data = {'state': ['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],
        'year': [2000,2001,2002,2003,2004,2005],
         'pop': [1.5,1.2,1.3,1.4,1.5,1.6]
       }
frame = pd.DataFrame(data)
frame
frame.head()
pd.DataFrame(data, columns=['year','state','pop'])frame2


# In[18]:


frame2 = pd.DataFrame(data, columns = ['year','state','pop','debt'],
                      index = ['one','two','three','four','five','six'])
frame2


# In[19]:


frame2.loc['three']


# In[9]:


from pandas import DataFrame
data = {'states':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],
        'year' : [2000,2001,2002,2001,2002,2003],
        'pop' : [1.5,1.7,3.6,2.4,2.9,3.2]
       }
frame = pd.DataFrame(data)
frame


# In[17]:


pd.DataFrame(data,columns=['year','state','pop'])
frame2 = pd.DataFrame(data, columns = ['year','pop','state','pop'],index = ['one','two','three','four','five','six'])
frame2
frame2.columns
frame2['debt'] = 16.5
frame2
val =pd.Series([-1.2,-1.5,-1.7], index= ['two','four','five'])
frame2['debt'] = val
frame2


# In[23]:


frame2['eastern'] = frame2.state == 'Ohio'
frame2
del frame2['eastern']
frame2
pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
frame3
frame.T


# In[24]:


pd.DataFrame(pop, index =[2001,2002,2003])


# In[25]:


pdata = {'Ohio': frame3['Ohio'][:-1], 'Nevada':frame3['Nevada'][:2]}
pd.DataFrame(pdata)


# In[ ]:




