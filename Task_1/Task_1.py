import cmath

# Question:-1
num1, num2, string1 = 10, 10.10, "string1"

print(num1, num2, string1)

# Question:-2
comp = complex(1,3)
num3 = 100

comp = 100
num3 = complex(1,3)
print(comp, num3)

# Question:-3
num4 = 40
num5 = 50
print(num4,num5)
temp = num4
num4 = num5
num5 = temp
print(num4,num5)

# Without Temp variable
num4, num5 = num5, num4
print(num4,num5)

# Question:-4
# x = raw_input("Enter value for x:- ")
y = input("Enter value for y:- ")
# print(x)
print(y)

# Question:-5
user_input1, user_input2 = input("Enter two values between 1 and 10 with space in between:- ").split()
z = int(user_input1) + int(user_input2) + 30
print(z)

# Question:-6
user_input3 = input("Enter anything you want:- ")
print("The data type of the input value is: ", type(user_input3))

# Question:-7
UpperCamelCase = "UpperCamelCase"
lowerCamelCase = "lowerCamelCase"
snake_case = "snake_case"
UPPERCASE = "UPPERCASE"

# Question:-8
a = 123
print(a)
a = "abc"
print(a)
#YES. Because Python variables are VALUE TYPE  
