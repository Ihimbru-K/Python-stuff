# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 23:38:26 2022

@author: mon pc
"""

#elementary operations on list of dictionaries
customers = [{"id" : 1, "name" : "Kanyimi"}, {"id" : 2, "name" :"Ihimbru"}, {"id": 3, "name":"Ihims"}]
for x in customers:
    print(x["id"], x["name"]) #iterate and print id and corresponding name
    
customers[2]["name"]= ["Aye"] #replace Ihims with Aye
print(customers)

del customers[1] #deleting the second dictionary
print(customers)
