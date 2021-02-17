#Question:-1

print("--------------QUESTION:- 1-----------------")

user_input = int(input("Enter the number:- "))

if(user_input % 3 == 0 and user_input % 5 == 0 ):
    print("Consultadd-Python Training")
elif(user_input % 3 == 0):
    print("Consultadd")
elif(user_input % 5 == 0):
    print("Python Training")


#Question:-2

print("--------------QUESTION:- 2-----------------")

num1, num2 = input("Enter two values with space in between:- ").split()
user_input2 = int(input("Enter the operation you would like to perform --> \n 1 for Addition, 2 for Subtraction, 3 for Division, 4 for Multiplication, 5 for Average:- "))
num1, num2, user_input2 = int(num1), int(num2), int(user_input2)

if(user_input2 == 1):
    print(num1 + num2)
elif(user_input2 == 2):
    print(num1 - num2)
    if((num1 - num2) < 0):
        print("NEGATIVE")
elif(user_input2 == 3):
    print(num1 * num2)
elif(user_input2 == 4):
    print(num1 / num2)
elif(user_input2 == 5):
    first, second = input("Enter two values with space in between:- ").split()
    first, second = int(first), int(second)
    print((num1 + num2 + first + second) / 4)


#Question:- 3

print("--------------QUESTION:- 3-----------------")

a, b, c = input("Enter two values for a, b,c with spaces in between:- ").split()
a, b, c = int(a), int(b), int(c)

avg = (a + b + c) / 3
print("avg = ", avg)

if(avg > a and avg > b and avg > c):
    print("avg is higher than a, b, c")
else:
    if(avg > a and avg > b):
        print("avg is higher than a and b")
    elif(avg > a and avg > c):
        print("avg is higher than a and c")
    elif(avg > b and avg > c):
        print("avg is higher than b and c")
    elif(avg > a):
        print("avg is just higher than a")
    elif(avg > b):
        print("avg is just higher than b")
    elif(avg > c):
        print("avg is just higher than c")
