import functools

print("--------------QUESTION:- 11-----------------")
#Question:- 11

result = filter(lambda x: x % 2 == 0, range(1,11))
#print(list(result))
Final_result = map(lambda x: x*x, result)
print(list(Final_result))

print("--------------QUESTION:- 12-----------------")
#Question:- 12

def divide(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Division by zero is not allowed!")
    else:
        print("Result is ", result)

#divide(100, 10)
divide(5, 0)

print("--------------QUESTION:- 13-----------------")
#Question:- 13

list_13 = [1,2,3,4,5,6,7]

joinedList = functools.reduce(lambda x, y:str(x) + str(y), list_13)
print(joinedList)

print("--------------QUESTION:- 14-----------------")
#Question:- 14

not_divisible_by3 = filter(lambda x: x % 3 != 0, range(1,100))
not_divisible_by3 =list(not_divisible_by3)

multiple_of7 = filter(lambda x: x % 7 == 0, not_divisible_by3)
print(list(multiple_of7))

print("--------------QUESTION:- 15-----------------")
#Question:- 15

map_15 = list(map(lambda x: x*x, range(1,10)))
print(map_15)

print("--------------QUESTION:- 16-----------------")
#Question:- 16

def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)#2

# def a():
#     try:
#         f(x,4)#"NameError: name 'f' is not defined"
#     finally:
#         print('after f')
#         print('after f?')
# a()
