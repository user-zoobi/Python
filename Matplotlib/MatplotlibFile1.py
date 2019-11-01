#!/usr/bin/env python
# coding: utf-8

# ## MATPLOTLIB

# Starting with Matplotlib

# In[19]:


import matplotlib.pyplot as plt
plt.plot([1,2,3],[3,1,2])
plt.show()


# In[12]:


import matplotlib.pyplot as plt
x = range(6)
plt.plot(x,[xi**2 for xi in x])
plt.show()


# In[17]:


import matplotlib.pyplot as plt
x = range(1,5)
plt.plot(x,[xi*1.5 for xi in x],x,[xi*3 for xi in x],x,[xi/4 for xi in x])
plt.show()


# In[28]:


import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,5)
plt.plot(x,x*1.5,x,x*2,x,x*3)
plt.xlabel("Time")
plt.ylabel("Distance")
plt.title("Chart")
plt.grid(True)
plt.show()


# In[29]:





# In[ ]:




