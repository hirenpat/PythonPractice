import cmath
import numpy as np

print("--------------QUESTION:- 1-----------------")
#Question:- 1
string_1 = "1234abcd"
reverse_string_1 = string_1[::-1]
print(reverse_string_1)

print("--------------QUESTION:- 2-----------------")
#Question:- 2
string_2 = "ABHfhfAHfh"
uper_char = 0
lower_char = 0
for x in string_2:
    if x.islower():
        lower_char += 1
    else:
        uper_char += 1
print("No of Uppercase characters: ", uper_char)
print("No of Lowercase characters: ", lower_char)


print("--------------QUESTION:- 3-----------------")
#Question:- 3
print("By using Traversal")
def unique_traversal(list3):
    unique_list3 = []

    for x in list3:
        if x not in unique_list3:
            unique_list3.append(x)
    
    print(unique_list3)

list3 = [1,2,3,3,4,5,5]
unique_traversal(list3)

print("By using Set")
def unique_set(list3):
    unique_set3 = set(list3)
    unique_list3 = (list(unique_set3))
    print(unique_list3)

list3 = [1,2,3,3,4,5,5]
unique_traversal(list3)

print("By using Numpy")
def unique_numpy(list3):
    unique_numpy= np.array(list3)
    print(np.unique(unique_numpy))

list3 = [1,2,3,3,4,5,5]
unique_traversal(list3)

print("--------------QUESTION:- 4-----------------")
#Question:- 4
user_input4 = input("Enter the hypen-seprated sequence: ").split("-")
user_input4.sort()
print("-".join(user_input4))


print("--------------QUESTION:- 5-----------------")
#Question:- 5
user_input5 = input("Enter the sequence: ")
print(user_input5.upper())


print("--------------QUESTION:- 6-----------------")
#Question:- 6

def sum(int1, int2):
    int1, int2 = int(int1), int(int2)
    print(int1 + int2)

int1 = input("Enter int 1: ")
int2 = input("Enter int 2: ")
sum(int1, int2)

print("--------------QUESTION:- 7-----------------")
#Question:- 7
def string_len(string1, string2):
    if len(string1) > len(string2):
        print(string1)
    elif len(string1) == len(string2):
        print(string1)
        print(string2)
string1 = input("Enter string1: ")
string2 = input("Enter string2: ")
string_len(string1, string2)

print("--------------QUESTION:- 8-----------------")
#Question:- 8
def tuple_8():
    list8 = []
    for x in range(21):
        list8.append(x*x)
    print(tuple(list8))

tuple_8()

print("--------------QUESTION:- 9-----------------")
#Question:- 9

limit = int(input("Enter the limit: "))
list_9 = []
limit += 1
def showNumbers(limit):
    for x in range(limit):
        if x % 2 == 0:
            list_9.append("Even")
        else:
            list_9.append("Odd")
    #print(list_9)
showNumbers(limit)
for index,item in enumerate(list_9):
    print(index,item)

print("--------------QUESTION:- 10-----------------")
#Question:- 10
result = filter(lambda x: x % 2 == 0, range(1,21))
print(list(result))
