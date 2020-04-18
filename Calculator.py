def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

print("Given operations are: \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide")
choice = int(input("Select operation from 1, 2, 3, 4: "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if (choice == 1):
    res = add(num1,num2)
    print(num1, "+", num2, "=", res)
elif (choice == 2):
    res = subtract(num1,num2)
    print(num1, "-", num2, "=", res)

elif (choice == 3):
    res = multiply(num1,num2)
    print(num1, "*", num2, "=", res)

elif (choice == 4):
    res = divide(num1,num2)
    print(num1, "/", num2, "=", res)

else:
    print("Invalid input")