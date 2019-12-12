#!/usr/bin/env python
# coding: utf-8

# ### {Deep Learning With Python}

# In[2]:


#Plotting a graph
import matplotlib.pyplot as plt
plt.plot([1,2,3],[3,1,2])
plt.show()


# In[3]:


import numpy as np
x = np.array(12)
x


# In[4]:


x.ndim


# In[6]:


x = np.array([12,3,4,5])
x
x.ndim


# In[4]:


import numpy as np
x = np.array([[12,3,4,5],
             [1,2,3,4],
             [2,3,4,5]]
                )
x


# In[5]:


x.ndim


# In[10]:


# from keras.datasets import mnist
# (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
# print(train_images.ndim)


# In[11]:


# print(train_images.shape)


# In[12]:


# print(train_images.dtype)


# In[10]:


import matplotlib.pyplot as plt
digit =train_images[4]
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()


# In[2]:


import matplotlib.pyplot as plt
my_slice = train_images[10:100]
print(my_slice.shape)


# In[4]:


import numpy as np
x = np.random.random((64,3,32,10))
y = np.random.random((32,10))
z = np.maximum(x,y)
z


# In[9]:


# import tensorflow as tf
# from keras.datasets import mnist
# (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
# train_images.shape


# In[8]:


# from keras.datasets import mnist
# (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
# print(train_images.ndim)


# In[7]:


# version tensorflow


# In[7]:


import tensorflow as tf
import matplotlib.pyplot as plt
digit = train_images[3]
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()


# ### Training the datasets of images

# The data has been train for te sequence of numbers 0-9 which has been training the system for 
# the set of 60000 images of about 28x28 by training and testing of datasets

# In[3]:


import tensorflow as tf
from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
train_images.shape


# In[4]:


len(train_labels)


# In[5]:


train_labels


# In[14]:


test_images.shape


# ### The network architecture

# In[15]:


from keras import models
from keras import layers
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))


# ### The compilation step

# In[16]:


network.compile(optimizer='rmsprop',
loss='categorical_crossentropy',
metrics=['accuracy'])


# ### Preparing the image data

# In[17]:


train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255


# ### Preparing the labels

# In[18]:


from keras.utils import to_categorical
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)
network.fit(train_images, train_labels, epochs=5, batch_size=128)


# In[19]:


test_loss, test_acc = network.evaluate(test_images, test_labels)


# In[20]:


print('test_acc:', test_acc)


# In[2]:


import tensorflow as tf
my_slice = train_images[10:100]
print(myslice.shape)


# In[1]:


print('images')


# In[ ]:




