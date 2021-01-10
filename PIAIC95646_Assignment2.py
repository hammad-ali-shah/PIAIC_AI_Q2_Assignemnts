#!/usr/bin/env python
# coding: utf-8

# # Numpy_Assignment_2::

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[5]:


import numpy as np
np.arange(10).reshape(2,5)


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::

# array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
# 

# In[8]:


arr1 = np.arange(10, dtype = 'int32').reshape(2,5)
arr2 = np.ones(10, dtype = 'int32').reshape(2,5)
np.vstack((arr1, arr2)) # tuple


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::

# array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
#        [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])

# In[9]:


arr1 = np.arange(10, dtype = 'int32').reshape(2,5)
arr2 = np.ones(10, dtype = 'int32').reshape(2,5)
np.hstack((arr1, arr2))


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::

# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# In[10]:


arr1 = np.array([[0,1,2,3,4], [5,6,7,8,9]])
arr1 = np.ravel(arr1)
arr1


# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::

# array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

# In[11]:


higher_to_lower = np.arange(15).reshape(3,5)
higher_to_lower.ravel()


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::

# array([[ 0, 1, 2],
# [ 3, 4, 5],
# [ 6, 7, 8],
# [ 9, 10, 11],
# [12, 13, 14]])

# In[12]:


one_to_higher = np.arange(15).reshape(5,3)
one_to_higher


# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[13]:


five_by_five = np.random.randint(1,10, (5,5))
print(five_by_five)
print('\nSQUARE')
np.square(five_by_five)


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[17]:


five_by_six = np.random.randint(1,11, (5,6))
np.mean(five_by_six)
# manually
# np.sum(five_by_six)/(5*6)


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[18]:


np.std(five_by_six)


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[19]:


np.median(five_by_six)


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[20]:



np.transpose(five_by_six)


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[21]:


four_by_four = np.arange(16).reshape(4, 4)
np.sum(np.diagonal(four_by_four))
# np.diag(four_by_four) ####### what is the diff?!?!
# print(np.sum(np.diagonal(four_by_four))) # same answer


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[22]:


np.linalg.det(four_by_four)


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[23]:


arr = np.arange(10)
np.percentile(arr, (5, 95))


# ## Question:15

# ### How to find if a given array has any null values?

# In[24]:


# generating an array 0-49 and 5 random null values (np.nan)
arr = np.arange(50, dtype=float).reshape(10, 5)
nulls = 5
null_indexes = np.random.choice(arr.size, nulls, replace =  False) 
# replace = False => NO REPEATED VALUES/ GIVES ONLY UNIQUE SAMPLES
# if replace = True (default) => sometimes the null_indexes might have duplicate values
# and we get less than 5 (nulls) np.nans
arr.ravel()[null_indexes] = np.nan
np.isnan(arr)
f'Total null values are {np.sum(np.isnan(arr))}'


# In[ ]:




