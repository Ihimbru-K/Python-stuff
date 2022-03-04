# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 22:57:50 2022

@author: mon pc
"""

#list methods in python
l = [1, 2, 3, 4, 5]
l.append(60)
print(l)

del(l[0])  #deletes the index position 1 in a list
l.pop()     #removes the last element from a list
l.pop(3)   #here, the third element in the list is removed
l.remove(4)   #element "4" is removed
print(l)
l.reverse() #reverses the order of elements in the list

y = [10, 20, 30, 40]
l.extend(y) # adds list y to list x
print(l)
l.reverse()
print(l)
l.sort() #sorts elements in ascending order
print(l)

