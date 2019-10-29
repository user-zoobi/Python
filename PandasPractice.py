#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from pandas import Series
obj = pd.Series([4,7,-5,3])
obj


# In[ ]:


obj.values
obj.index


# In[ ]:


import pandas as pd 
from pandas import Series
obj2 = pd.Series([0,1,2,3,4,5,6,7,8,9])
obj2.index = [['a','b','c','d','e','f','g','h','i','j']]
obj2.values , obj2.index


# In[ ]:


obj2[['a','b','c','e']]


# In[ ]:


apples = pd.Series([3,2,0,1],index = ['a','b','c','d'])
oranges = pd.Series([2,0,1,3],index = ['e','f','g','h'])
data = {'apples': apples , 'oranges' : oranges}
fruits = pd.DataFrame(data)
fruits


# In[ ]:


fruits.head()


# In[ ]:


pd.DataFrame(data,rows=[apples,oranges])


# In[ ]:


data = {'data1' : ['Ohio','Frankfurt','Berlin','Karachi','Tokyo','Beijing'],
       'data2' : [2000 , 2001 , 2002 , 2004 , 2005 ,2006] , 'data3' : [1.2,1.3,1.4,1.5,1.6,1.7]  }
frame = pd.DataFrame(data)
frame


# In[ ]:


frame.head()


# In[ ]:


pd.DataFrame(data,columns = ['data2','data1','data3'])

