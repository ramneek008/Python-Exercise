list = ["butter", "cream", "apple"]
print("list: ")
print(list)

list1 = [["apple","mango"],"almond"]
print("Multi-dimensional list")
print(list1)

list2 = []
list2.append(1)
list2.append(2)
list2.append(3)
print("List2: ",list2)
list2.append(list)
print("appending list to list2: ",list2)

list2.insert(1,12)
print("Inserting at position 1: ",list2)

list2.extend([3,4,"great"])
print("Extending list2 : ",list2)


sea_creatures = ['shark','cuttlefish','squid','mantisshrimp','anemone']
print(sea_creatures)
print(len(sea_creatures))

l = []
l.append(10)
print(l)
l.append('Hello')
print(l)
l.append(True)
print(l)

#nested list
nested_list = ['Happy',[2,0,2,0]]
print(nested_list)
print(nested_list[0])

