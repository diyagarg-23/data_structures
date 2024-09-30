#!/usr/bin/env python
# coding: utf-8

# # LIST

# In[19]:


#Lists
#creating a list
List = []
print(List)

#creating a list of numbers
List1 = [12,34,45]
print(List1)
print(type(List1))
#list can store heterogeneous and duplicate data
#there is positive as well as negative indexing


# In[6]:


#creating a list of strings and accessing using index
list2 = ['u','r','amazing']
print(list2[0])
print(list2[-1])


# In[9]:


List = [1,2,4,4,3,3,3,5,6]
print(List)


# In[10]:


#list methods
mylist = ['maths','english',92,97]
mylist.append(199)  #used for adding elements to the end of the list
print(mylist)


# In[11]:


mylist = ['maths','english',92,97]
mylist.insert(2,134) #insert at 2nd position
print(mylist)


# In[13]:


list1 = [1,2,3]
list2 = [2,3,4,5]

#add list2 to list1
list1.extend(list2)
print(list1)

#add list1 to list2 now
list2.extend(list1)
print(list2)

#lists are mutable i.e changes happen in original list


# In[14]:


list = [1,2,3,1,2,1,2,3,2,1]
print(list.count(1))


# In[16]:


list = [2.3,4.445,3,5.33,1.054,2.5]
print(list.pop())
print(list.pop(1))
print(list)


# In[17]:


#functions
numbers = [5,2,8,1,9]
print(min(numbers))


# In[18]:


list = [2.3,4.445,3,5.33,1.054,2.5]
del list[0]
print(list)

#by using pop we can see what we are deleting rather than using delete


# # TUPLE

# In[20]:


#tuples are immutable list


# In[21]:


#creating tuple
tuple = ('apple','banana','cherry')
print(tuple)


# In[22]:


tuple = 'apple','banana'
type(tuple)


# In[23]:


tuple=()
print(tuple)


# In[24]:


onetuple = ('apple',)
print(onetuple)
type(onetuple)


# In[25]:


#creating a tuple with nested tuples
tuple1 = (1,2,3,4)
tuple2 = ('python','java')
tuple3 = (tuple1,tuple2)
print("\ntuple with nested tuples: ")
print(tuple3)


# In[26]:


tuple1 = (1,2,3,4)
tuple2 = ('python','java')
tuple3 = tuple1 + tuple2
print(tuple3)


# In[31]:


# Ensure no redefinition of 'tuple'
# If you previously assigned 'tuple' to something else, we use del to fix that
del tuple  # This restores the built-in tuple function, if redefined

# Slicing a tuple
tuple1 = tuple('REPUBLICOFINDIA')

# Removing first element
print('Removal of first element: ')
print(tuple1[1:])

# Reversing the tuple
print('Tuple after sequence of elements is reversed: ')
print(tuple1[::-1])

# Printing elements in the range
print('Printing elements between range 4-9: ')
print(tuple1[4:9])


# In[1]:


#creating tuples
Tuple = (0,1,(2,3),(2,3),1,[3,2],'geeks',(0,))

#count the appearance of (2,3)
res = Tuple.count((2,3))
print('count of (2,3) in tuple is: ',res)


# In[2]:


#creating tuple
tuple = (0,1,2,3,2,3,1,3,2)

#getting the index of 3
res = tuple.index(3)
print('first appearance of 3 is: ',res)

#getting the index of 3 after 4th index
res = tuple.index(3,4)
print('first occurence of 3 after 4th index is: ',res)


# # DICTIONARY
# 

# In[3]:


#a dictionary in python is a data structure that stores the
#value in key:value pairs. Dictionaries are mutable


# In[4]:


dict1 = {}
print('empty dictionary: ')
print(dict1)


# In[5]:


dict = {1: 'python', 2: 'java', 3: 'react'}
print(dict)


# In[8]:


#nested dictionaries
dict = {1: 'geeks', 2: 'for',
       3: {'A': 'welcome', 'B': 'To', 'C': 'Python'}}

print(dict)
print(dict[3]['A'])#accessing nested elements


# In[9]:


#accessing dictionary elements

dict = {1: 'Python', 'name': 'For', 3: 'Beginners'}
print('accessing an element using key: ')
print(dict['name'])
print('accessing an element using key: ')
print(dict[1])

#using get method

print('accessing an element using get: ')
print(dict.get(3))


# In[1]:


#add items to a python dictionary with different datatypes
dict = {}
print('empty dictionary: ')
print(dict)

dict[0] = 'python'
dict[2] = 'for'
dict[3] = 1
print('\ndictionary after adding 3 elements: ')
print(dict)

dict['value_set'] = 2,3,4
print('\ndictionary after adding 3 elements: ')
print(dict)

dict[2] = 'welcome'
print('\nupdated key value: ')
print(dict)
dict[5] = {'nested': {'1': 'life', '2': 'beginners'}}
print('\nadding a nested key: ')
print(dict)


# In[2]:


#dictionary methods
dict1 = {1: 'Monika', 2: 'Martina', 3: 'Stefi', 4: 'Maria'}
dict2 = dict1.copy()
print(dict2)

dict1.clear()
print(dict1)
print(dict2.get(1))
print(dict2.items()) #returns a list containing a tuple for each key value pair
print(dict2.keys()) #returns a list containing dictionary's keys
(dict2.pop(4)) #reoves the element with specified key
print(dict2)
dict2.popitem() #removes the last inserted key-value pair
print(dict2)
dict2.update({3: 'Serena'})
print(dict2)
print(dict2.values()) #updated the dict2 values


# In[1]:


original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#slicing the dictionary to include only keys 'a' and 'c'
sliced_dict = {k: original_dict[k] for k in ['a','c']}
print(sliced_dict) #output: {'a': 1, 'c': 3}


# # SET

# In[9]:


#a set in python programming is an unordered 
#collection of unique element
emptyset = set()
type(emptyset)


# In[10]:


var = {'India', 'is', 'great'}
type(var)
print(var[1]) #error because can't be accessed through index


# In[16]:


#adding elements to the set
#sets are mutable
myself = {'a','b',}
myself.add('d') #anyehere
print(myself)


# In[17]:


#sets are define
A = {0,2,4,6,8}
B = {1,2,3,4,5}
C = set()
print(type(C))

#set operations

#union
print('union: ',A | B)

#intersection
print("intersection: ",A & B)

#difference
print('difference: ',A - B)

#symmetric difference #A-B union B-A
print('symmetric difference: ',A ^ B)


# In[18]:


#set of letters
s = {'g','e','k','s'}

#adding 'f'
s.add('f')
print('set after updating: ',s)

#discarding element from set
s.discard('g')
print('\nset after updating: ',s)

#removing elemnet from set
s.remove('e')
print('\nset after updating: ',s)

#popping elements from set
print('\npopped element: ',s.pop())
print('set after updating: ',s)

s.clear()
print('set after updating: ',s)

#typecasting list to set
myset = set(['a','b','c'])
print(myset)


# In[19]:


#creating frozensets ->immutable
frozenset1 = frozenset([1,2,3])
frozenset2 = frozenset([4,5,6])

#creating a set of frozensets
nested_set = {frozenset1, frozenset2}

print(nested_set)


# In[20]:


#set slicing work around
original_set = {1,2,3,4,5}

#convert set to a list and slice it
sliced_list = list(original_set)[:3]
print(sliced_list) #output can be any since sets are unordered


# In[ ]:




