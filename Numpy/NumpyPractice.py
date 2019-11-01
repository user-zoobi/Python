#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
x = [12,11,10,19]
data = np.array(x)
print(data)


# In[2]:


x = [.06,.05,.03,.07]
data = np.array(x)
print(data)


# In[3]:


x = ([1,2,3],[2,3,4])
data = np.array(x)
print(data)


# Updates about the image to numpy assignments
# 
# you need to download 20 photos and save in the photos folder
# 
# use the following codes to scan the folder (change folder name from '.' to photos
# 
#  Import the os module, for the os.walk function
#  
# import os
# 
# Set the directory you want to start from
# 
# rootDir = '.'
# for dirName, subdirList, fileList in os.walk(rootDir):
# print('Found directory: %s' % dirName)
# for fname in fileList:
# print('\t%s' % fname)
# print('Found directory: %s' % dirName)
# to for fname in fileList:e name (with input) as input and load it and resize it to 200, 200, 3)  
# 
# and return a numpy array. you need an image resize library like PIL
# 
# 4) store this numpy array of the image into the main array (created earlier in the code with 20, 200, 200, 3 dimensions 
# 
# Note: you can find some partial code in this group

# In[9]:


x = [2.099999999,3,4,5,6]
y = [8,9,0,5,3]
xx = np.array(x,dtype = np.int32 )
yy = np.array(y,dtype = np.float64 )
print(xx)


# In[16]:


x = np.array([1,2,3,4,5,6])
y = np.array([4,5,6,7,9,0])
data = x*y
print(data)


# In[7]:


import numpy as np
x = np.arange(10)
print(x[:])


# In[25]:


arr1 = [(0,1),(1,3),(2,4)]
arr2 = [(4,3),(5,2),(6,1)]
arr3 = [(7,9),(8,2),(9,0)]
print(int(arr1[0][0])*int(arr2[0][1]))


# In[28]:


y = ['Melissa']
x = ['Bob','Dwayne','Melissa','Tim','Sila']
a = np.array(x)
b = np.array(y)
a==b


# In[37]:


np.arange(0:5:1)


# In[39]:


points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
ys


# In[1]:


import numpy as np
array1 = np.empty((12,5))
for x in range(12):
    array1(x) = x 
    
print(array1)


# In[12]:


import numpy as np
x = np.arange(10)
print(x)
data = [
    x[0:2],
    x[0:3],
    x[4:8]
]
data


# In[13]:


names = np.array(['bob','smith','sammy','bill','tom','marsh','ben'])
names[0:4]


# In[18]:


import numpy as np
names = np.array(['bob','smith','sammy','bill','tom','marsh','ben'])
data = np.random.randn(6,4)
data


# In[21]:


array = np.array([ array[1,2,3],array[2,3,4],array[4,7,8]
                   array[0,1,0],array[9,7,8],array[9,3,4]
                   array[2,3,5],array[5,6,7],array[7,8,9] ])
array1 = [array[0][2], array[0][1],
          array[1][1], array[1][2] ]
array1


# In[31]:


import numpy as np
array1 = np.arange(60).reshape(6,5,2)
array1


# In[29]:


array1.transpose()


# In[12]:


from PIL import Image
img  = Image.open('airplane.png') 
try:  
    img  = Image.open('airplane.png')  
except IOError: 
    pass


# In[ ]:


from PIL import Image 
  
filename = "airplane.png"
with Image.open(filename) as image: 
    width, height = image.size
    image.show()


# In[3]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img=mpimg.imread('airplane.png')
imgplot = plt.imshow(img)
plt.show()


# In[4]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img=mpimg.imread('airplane.png')
imgplot = plt.imshow(img)
plt.imshow(np.fliplr(img))
plt.show()


# In[3]:


import numpy as np
x = np.array([2,3,4,5])
x


# In[9]:


import numpy as np

data = np.array([[1,2,3,4,5],[2,3,4,5,5]])

data3 = data*data
data3



# In[10]:


data > data3


# In[15]:


data = np.array([1,2,3,4,5])
data[2:-1]


# In[18]:


data = np.arange(10)
data[5]
data[5:8]

