#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:20:05 2019

@author: pinchun
"""

import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

json_dumps = json.dumps(data)
print(type(data))           # dict
print(type(json_dumps))     # str
print("json.dumps transfer dict to str")

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
print("json.dump transfer dict to str and write to a file")
    

with open('data.txt') as json_file:
    data2 = json.load(json_file)     
print("json.load read string from file, transfer it to dict")
    
print(type(data2))      # dict

json_loads = json.loads(json_dumps)
print(type(json_dumps))     # str
print(type(json_loads))     # dict
print("json.loads transfer str to dict")
    
for p in data2['people']:
    print('Name: ' + p['name'])
    print('Website: ' + p['website'])
    print('From: ' + p['from'])
    print('')
    
# Pretty-Printing
print(json.dumps(data, indent=4))
