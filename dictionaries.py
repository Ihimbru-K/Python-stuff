# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 23:08:51 2022

@author: mon pc
"""


#Dictionary data type

data = {"school": "NAHPI", "DB": 2002, "bread": [200, 2]}

for items in data.keys():
    print(items)
for items in data.values():
    print(items)
    
for key in data:
    print(key, data[key]) #iterate and print keys and values

x = data["school"]
print(x) #print value of school key

print(data.keys())
print(data.items())

print(data.pop("school"))

