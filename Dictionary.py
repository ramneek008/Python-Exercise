
dict = {}
print(type(dict))

dict = {1:'abc',2:'efg','name':'xyz'}
print(dict)

print(dict[1])
print(dict['name'])

dict1 = {1:'abc',2:'efg','name':'xyz'}
dict1['name'] = 'main'
dict1['age'] = '22'
print(dict1)

#deleting elements
del dict1['name']
print(dict1)

dict1.clear()
print(dict1)

del(dict1)
#print(dict1)

print(dir(list))  #displays all funtions related to list


#no duplicate
dict1 = {1:'abc',2:'efg','name':'xyz', 2: 'mul'}
print(dict1)

##Dictionary sorting
dict1 = {1:'abc',2:'efg','name':'xyz'}
print(dict1.keys())
print(dict1.values())
print(dict1.items())
#d=eval(input('Enter Dictionary'))
#print(type(d))



import operator

d={'c':1, 'b':5,'a':3}
sorted_key = sorted(d.items())
print(sorted_key)

sorted_value = sorted(d.items(), key=operator.itemgetter(1))
print(sorted_value)
