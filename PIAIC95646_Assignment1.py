#!/usr/bin/env python
# coding: utf-8

# # **Assignment For Numpy**

# Difficulty Level **Beginner**

# 1. Import the numpy package under the name np

# In[2]:


import numpy as np


# 2. Create a null vector of size 10 

# In[3]:


null_vector = np.zeros(10)


# 3. Create a vector with values ranging from 10 to 49

# In[4]:


arr = np.arange(10,49)


# 4. Find the shape of previous array in question 3

# In[5]:


arr = np.arange(10,49)
np.shape(arr)


# 5. Print the type of the previous array in question 3

# In[6]:


arr = np.arange(10,49)
arr.dtype


# 6. Print the numpy version and the configuration
# 

# In[7]:


np.__version__


# In[8]:


np.show_config()


# 7. Print the dimension of the array in question 3
# 

# In[9]:


arr = np.arange(10,49)
arr.ndim


# 8. Create a boolean array with all the True values

# In[10]:


ar = np.ones(10, dtype = bool)
ar


# 9. Create a two dimensional array
# 
# 
# 

# In[11]:


b = np.arange(12).reshape(4,3)
b


# 10. Create a three dimensional array
# 
# 

# In[12]:


c = np.arange(24).reshape(2,3,4)
c


# Difficulty Level **Easy**

# 11. Reverse a vector (first element becomes last)

# In[13]:


arr = np.arange(1,10)
arr


# 12. Create a null vector of size 10 but the fifth value which is 1 

# In[14]:


arr = np.arange(1,10)
arr[::-1]


# 13. Create a 3x3 identity matrix

# In[17]:


x = np.arange(2, 11).reshape(3,3)
print(x)


# 14. arr = np.array([1, 2, 3, 4, 5]) 
# 
# ---
# 
#  Convert the data type of the given array from int to float 

# In[18]:


arr = np.array([1, 2, 3, 4, 5])
arr.astype(float)


# 15. arr1 =          np.array([[1., 2., 3.],
# 
#                     [4., 5., 6.]])  
#                       
#     arr2 = np.array([[0., 4., 1.],
#      
#                    [7., 2., 12.]])
# 
# ---
# 
# 
# Multiply arr1 with arr2
# 

# In[19]:


arr1 = np.array([[1., 2., 3.],[4., 5., 6.]])
arr2 = np.array([[0., 4., 1.],[7., 2., 12.]])
arr1 * arr2


# 16. arr1 = np.array([[1., 2., 3.],
#                     [4., 5., 6.]]) 
#                     
#     arr2 = np.array([[0., 4., 1.], 
#                     [7., 2., 12.]])
# 
# 
# ---
# 
# Make an array by comparing both the arrays provided above

# In[20]:


arr1 = np.array([[1., 2., 3.],[4., 5., 6.]])
arr2 = np.array([[0., 4., 1.],[7., 2., 12.]])

comparison = arr1 == arr2
equal_arrays = comparison.all()          # All() To check if 2 arrays are equal
equal_arrays


# 17. Extract all odd numbers from arr with values(0-9)

# In[21]:


arry1 = np.arange(9)
for item in arry1:
    if item % 2 > 0:
        print(item)


# 18. Replace all odd numbers to -1 from previous array

# In[22]:


arry1 = np.arange(9)
for item in arry1:
    if item % 2 > 0:
        item = -1
        print(item)


# 19. arr = np.arange(10)
# 
# 
# ---
# 
# Replace the values of indexes 5,6,7 and 8 to **12**

# In[23]:


arr = np.arange(10)
arr[5] = 12
arr[6] = 12
arr[7] = 12
arr[8] = 12
for item in arr:
    print(item)


# 20. Create a 2d array with 1 on the border and 0 inside

# In[25]:


b = np.arange(12).reshape(4 ,3)
b[0 , 0] = 1
b[0 , 2] = 1
b[1 , 0] = 1
b[1 , 2] = 1
b[2 , 0] = 1
b[2 , 2] = 1
b[3 , 0] = 1
b[3 , 2] = 1
b[3 , 1] = 1
b[1 , 1] = 0
b[2 , 1] = 0
b


# Difficulty Level **Medium**

# 21. arr2d = np.array([[1, 2, 3],
# 
#                     [4, 5, 6], 
# 
#                     [7, 8, 9]])
# 
# ---
# 
# Replace the value 5 to 12

# In[27]:


arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d[1,1]=12
arr2d


# 22. arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# 
# ---
# Convert all the values of 1st array to 64
# 

# In[31]:


arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d[1,0,0]=64
arr3d[1,0,1]=64
arr3d[1,0,2]=64
arr3d[1,1,0]=64
arr3d[1,1,1]=64
arr3d[1,1,2]=64
print(arr3d)


# 23. Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it

# In[32]:


b = np.arange(9).reshape(3,3)
b[0]


# 24. Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it

# In[33]:


arr = np.arange(0,9)
arr.reshape(3,3)
arr[1]


# In[ ]:





# 25. Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows

# In[36]:


arr = np.arange(9).reshape(3,3)
arr


# In[69]:


arr[0]


# In[70]:


arr[1]


# 26. Create a 10x10 array with random values and find the minimum and maximum values

# In[71]:


arr = np.random.randint(100, size=(10,10))
arr


# In[72]:


print(np.min(arr))
print(np.max(arr))


# 27. a = np.array([1,2,3,2,3,4,3,4,5,6]) b = np.array([7,2,10,2,7,4,9,4,9,8])
# ---
# Find the common items between a and b
# 

# In[43]:


a = np.array([1,2,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
r = np.intersect1d(a,b)
r


# 28. a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# 
# ---
# Find the positions where elements of a and b match
# 
# 

# In[44]:


a = np.array([1,2,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
r = np.intersect1d(a,b)
print(r)


# 29.  names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])  data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will**
# 

# In[47]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.rand(7, 4)
data[names != "Will"]


# 30. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will** and **Joe**
# 
# 

# In[48]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
print(data[names != "Will"])
print(data[names != "Joe"])


# Difficulty Level **Hard**

# 31. Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15.

# In[49]:


arr = np.random.randn(1,15).reshape(5,3)
arr


# 32. Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16.

# In[51]:


data = np.random.randn(1, 16).reshape(2,2,4)


# 33. Swap axes of the array you created in Question 32

# In[53]:


data = np.random.randn(1, 16).reshape(2,2,4)
data.T


# 34. Create an array of size 10, and find the square root of every element in the array, if the values less than 0.5, replace them with 0

# In[54]:


r =  np.arange(10)
r = np.sqrt(r)
np.where(r<0.5,0,r)


# 35. Create two random arrays of range 12 and make an array with the maximum values between each element of the two arrays

# In[55]:


a = np.random.randint(12)
b = np.random.randint(12)
np.maximum(a,b)


# 36. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# 
# ---
# Find the unique names and sort them out!
# 

# In[56]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
names


# In[57]:


names = set (names)
names


# 37. a = np.array([1,2,3,4,5])
# b = np.array([5,6,7,8,9])
# 
# ---
# From array a remove all items present in array b
# 
# 

# In[62]:


a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
result = np.setdiff1d(a, b)
print(result)


# 38.  Following is the input NumPy array delete column two and insert following new column in its place.
# 
# ---
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
# 
# 
# ---
# 
# newColumn = numpy.array([[10,10,10]])
# 

# In[63]:


saArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
saArray[2:] = ([[10,10,10]])
saArray


# 39. x = np.array([[1., 2., 3.], [4., 5., 6.]]) y = np.array([[6., 23.], [-1, 7], [8, 9]])
# 
# 
# ---
# Find the dot product of the above two matrix
# 

# In[64]:


x = np.array([[1.,2.,3.,],[4.,5.,6.,]])
y = np.array([[6.,23.],[-1.,7.],[8,9]])
np.dot(x,y)


# 40. Generate a matrix of 20 random values and find its cumulative sum

# In[67]:


A = np.random.randint(20, size=(4,4))
A


# In[68]:


np.sum(A)


# In[ ]:




