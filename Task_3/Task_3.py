import cmath

print("--------------QUESTION:- 1-----------------")
#Question:- 1

list_1 = [123, 34, 30, complex(1,3), complex(3,5), 3.4, 3.3, "hi", "hello", "world"]
print(list_1)

print("--------------QUESTION:- 2-----------------")
#Question:- 2

list_2 = ["hi", "hello", "world", ]
print(list_2[:2])
print(list_2[2:])

print("--------------QUESTION:- 3-----------------")
#Question:- 3

list_3 = [1,2,3,4,5]
list3_sum = 0
list3_mul = 1
for x in list_3:
    list3_sum += x
    list3_mul *= x

print(list3_sum)
print(list3_mul)

print("--------------QUESTION:- 4-----------------")
#Question:- 4

list_4 = [1,2,3,4,5]
print(min(list_4))
print(max(list_4))

print("--------------QUESTION:- 5-----------------")
#Question:- 5

list_5 = [1,2,3,4,5]
for x in list_5:
    if x % 2 == 0:
        list_5.remove(x)
print(list_5)

print("--------------QUESTION:- 6-----------------")
#Question:- 6
list_6 = []
for x in range(1,31):
    if(x < 6 or x > 24):
        list_6.append(x*x)
    else:
        list_6.append(x)
print(list_6)

print("--------------QUESTION:- 7-----------------")
#Question:- 7
list_7 = [1,2,3,4,5]
list_7a = [6,7,8,9,10]

list_7.remove(list_7[-1])
list_7.extend(list_7a)
print(list_7)

print("--------------QUESTION:- 8-----------------")
#Question:- 8
dict_8 = {'a':10, 'b':20}
dict_8a = {'c':30, 'd':40}
final_dict_8 = dict_8.update(dict_8a)
print(dict_8)

print("--------------QUESTION:- 9-----------------")
#Question:- 9
dict_9 = {}
num = int(input("Enter the value of n :- "))
for x in range(num):
    n = x + 1
    dict_9.update({n : n*n})
print(dict_9)

print("--------------QUESTION:- 10-----------------")
#Question:- 10
user_input = input("Enter a sequence of comma-separated numbers:- ").split(",")
list_10 = []
tuple_10 = ()
for x in user_input:
    list_10.append(x)
    temp = list(tuple_10)
    temp.append(x)
    tuple_10 = tuple(temp)
print(list_10)
print(tuple_10)
