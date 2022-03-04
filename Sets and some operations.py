# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 22:01:40 2022

@author: mon pc
"""

#some set operations
#A set is a collection which is unordered and unindexed with no duplicate elements. In Python sets
#are written with curly brackets
#it is an immutable data type unlike lists and others


x = {"a", "b", "c", "d", 2, 4, 5}
y = {1, 2, 3, 4, 5,6}

print(len(x)) #length of set x

x.add("e")#an element can be added in a set using add() method
print(x)

x.update(y)#multiple elements are added in a set using the update() method
print(x)

x = y.copy() #return a copy of set
print(x)

y.discard(6) #remove element 6 in set
print(y)


z = x.union(y) #return a new set z as a union of x and y
print(z) 

a = x.difference(y) #return a new set as a difference of x and y
print(a)

z = x.difference_update(y)
print(z)

t = x.intersection(y)
print(t)

f = x.intersection_update(y) #used to update a set f with the intersection of x and y
print(f)

x.clear() #used to remove all elements from set x
print(x)

