set1 = set("AppleMangoBanana")
print("Set1: ",set1)

set2 = set(["Apple", "Mango", "Apple"])
print("Set2 using list: ", set2)

set3 = set([1,3,4,4,2,4,5])
print('Set3 using numbers: ',set3)

set4 = set()
set4.add(3)
set4.add(1)
set4.add(5)
set4.add((1,2))
print("Set4 using add func: ",set4)



s=set()
print(type(s))

s=set([1,2,3,4])
print(s)

s={}
print(type(s))  #dictionary

s= {1,2,3,1,2}
print(s)


l = [1,2,3,4,5,2,3,1]
s=set(l)
print(s) 

l=[6,7,8,9,1,2,3,4,6,7,3]
s=set(l)
print(s)
# print(s[1])   gives error bcoz  sets are not subscriptable
s.add(7)
print(s)
s.update([10,11])
print(s)
s.discard(4)
print(s)
#s.remove(5)
print(s)

s = {1,2,3,4,5,6,7}
s.pop()
print(s)
s.pop()
print(s)


set1 = {1,2,3}
set2 = {3,4,5}

#union
print(set1.union(set2))
print(set1 | set2)

#intersection
print(set1.intersection(set2))
print(set1 & set2)

#difference
print(set1 - set2)
print(set1.difference(set2))

#symmetric difference
print(set1 ^ set2)
print(set1.symmetric_difference(set2))