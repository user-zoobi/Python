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


# In[6]:


from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print(train_images.ndim)


# In[7]:


print(train_images.shape)


# In[8]:


print(train_images.dtype)


# In[10]:


import matplotlib.pyplot as plt
digit =train_images[4]
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()


# In[ ]:




