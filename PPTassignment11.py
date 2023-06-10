#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Answer1. 

def mySqrt(x):
    if x == 0:
        return 0
    
    left = 1
    right = x
    
    while left <= right :
        mid = left + (right - left) // 2
        if mid * mid  == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
            
    return right


# In[2]:


input = 4
result = mySqrt(input)
print(result)


# In[3]:


input = 8
result = mySqrt(input)
print(result)


# In[25]:


#answer 2.
def PeakElement(num):
    for i in range(len(num) - 1):
        if num[i] > num[i - 1] and num[i] > num[i + 1]:
            return num[i]


# In[26]:


input = [1, 2, 3, 1]
result = PeakElement(input)
print(result)


# In[28]:


input = [1,2,1,3,5,6,4]
result = PeakElement(input)
print(result)


# In[3]:


#Answer 3.

def missingNumber(nums):
    n = len(nums)
    missing = n 
    
    for i in range(n):
        missing ^= i ^ nums[i]
        
    return missing


# In[4]:


input = [3, 0, 1]
result = missingNumber(input)
print(result)


# In[5]:


input = [0, 1]
result = missingNumber(input)
print(result)


# In[6]:


input = [9,6,4,2,3,5,7,0,1]
result = missingNumber(input)
print(result)


# In[7]:


#Answer 4.

def FindDup(nums):
    count = {}
    
    for num in nums:
        if num in count:
            return num
        count[num] = 1
        
    return None


# In[8]:


num = [1, 3, 4, 2, 2]
result = FindDup(num)
print(result)


# In[11]:


num = [3, 1, 3, 2, 2]
result = FindDup(num)
print(result)


# In[12]:


#Answer 6.

def FindMin(num):
    return min(num)


# In[13]:


num = [3, 4, 5, 1, 2]
result = FindMin(num)
print(result)


# In[14]:


num = [4,5,6,7,0,1,2]
result = FindMin(num)
print(result)


# In[15]:


num = [11,13,15,17]
result = FindMin(num)
print(result)


# In[16]:


#Answer 7.

def Range(num, target):
    start = -1
    end = -1
    
    if target in num:
        start = num.index(target)
        end = len(num) - 1 - num[::-1].index(target)
        
    return [ start, end]


# In[18]:


num = [ 1, 2, 2, 4, 4 , 4, 7, 8]
target =4
result =Range(num, target)
print(result)


# In[33]:


num = []
target = 0
result = Range(num, target)
print(result)


# In[45]:


#Answer 8.

def Intersect(num1, num2):
    intersection = []
    count = {}
    
    for num in num1:
        count[num]= count.get(num, 0) + 1
        
    for num in num2:
        if num in count and count[num] > 0:
            intersection.append(num)
            count[num] -= 1
            
            
    return intersection


# In[48]:


num1 = [1, 2, 2, 1]
num2 = [2, 2]
intersection = Intersect(num1 , num2)
print(intersection)


# In[50]:


num1 = [4, 9, 5]
num2 = [9, 4, 9, 8, 4]
intersection = Intersect(num1 , num2)
print(intersection)


# In[ ]:




