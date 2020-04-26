string = "Python practice going on"
print(string)

print("First character of string is: ")
print(string[0])

print("Last character of string is: ")
print(string[-1])

print("slicing elements from 3-14: ")
print(string[3:14])

string1 = '''Hi, I'm "Ramneek"'''
print("String1: ")
print(string1)

string2 = "{} {} {}".format('Be', 'Honest', 'always')
print("String2 in default order: ")
print(string2)

string3 = "{1} {0} {2}".format('Be', 'Honest', 'always')
print("String3 in positional order: ")
print(string3)

s = "We are learning python"

print(s.upper())

print(s.lower())

s='We are learning python     '
print(s.strip())          #removes extra spaces

s = 'We are learning python'
print(s.find('are'))
print(s.find('java'))
b = s.replace("learning",'teaching')
print(b)

split_string = s.split(' ')
print(split_string)
print(type(split_string))   #list

print(' '.join(split_string))
joined_string = ','.join(split_string)
print(joined_string)

print(s)
print(s[0])

s='programming'
print(s[-7:-3])
print(s[::2])

s = 'ha@ha@ha@'
print(s[::3])