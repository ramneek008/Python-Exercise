tuple1 = ('apple', 'banana')
print("Tuple1: ",tuple1)

list = [1,2,3,4,5]
print("Tuple using list: ", tuple(list))

tuple2 = tuple('Great')
print("Using tuple function: ", tuple2)

a,b,c,d,e = tuple2
print("After unpacking: ")
print(a)
print(b)
print(c)
print(d)
print(e)

tuple3 = ('Geeks',) * 3
print("Tuple with repitition: ", tuple3)

tuple4 = tuple('GoodPython')
print("Tuple4: ",tuple4)
print("After reversing: ", tuple4[::-1])


t = (1,2,3)
print(type(t))
t=(1,2,'hi',3)

t=(1)
print(type(t))  #int 

t=(1,)   # t=1,
print(type(t))  #tuple

t=('python')
print(type(t)) #string

t=('python',)
print(type(t))  #tuple

t = (1,2,3,(4,5),[6,7,8])
t[4][0] = 11  # only list is mutable
print(t)

t=(1,2,3)
# t.append(4)   gives error bcoz tuple is immutable



#convert a list to tuple
l=[0,1,2]
print(tuple(l))
print(tuple('Python'))


t = (1,2,3,4,5,6,7,8,1,2,3)
print(t.count(1))
print(t.index(3))
print(len(t))
print(min(t))
print(max(t))
print(sum(t))

