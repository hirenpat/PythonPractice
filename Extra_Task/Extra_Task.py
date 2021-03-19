
# #Question:-1

print("--------------QUESTION:- 1-----------------")

x = [100, 200, 300, 400,500, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 600, 700, 800]

print(x[5][:4])
#[1,2,3,4]

print(x[6:8])
#[600, 700]

print(x[::2])
#[100, 300, 500, 600, 800]

print(x[::-1])
#[[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]

print(x[5][5][0])
#[10]

print(x[0:0])
#[]

# #Question:-2

print("--------------QUESTION:- 2-----------------")
# import sys

# a = range(1, 10000)
# print(sys.getsizeof(a))
# b = xrange(1, 10000)
# print(sys.getsizeof(b))

# #Question:-3

print("--------------QUESTION:- 3-----------------")

#List is mutable and Tuple is immutable in python. So when we don't want other to change or modify something then we can use Tuple instead of List

# #Question:-4

print("--------------QUESTION:- 4-----------------")

for x in range(1, 100):
    if(x%3 == 0) and (x%2 == 0):
        print(x)

# #Question:-5

print("--------------QUESTION:- 5-----------------")

string_5 = "hiren"
result = ""
for index, item in enumerate(string_5):
    result = item + result
    if item in "aeiou":
        print(index)
print(result)

# #Question:-6

print("--------------QUESTION:- 6-----------------")

words = "hello my name is abcde"
words = words.split() 
for word in words:
    if len(word) % 2 == 0:
        print(word)


# #Question:-7

print("--------------QUESTION:- 7-----------------")

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
result = 8
n = len(x)

for i in range(0, n):
    for j in range(i+1, n):
        pair = []
        if x[i] + x[j] == result:
            pair.append(x[i])
            pair.append(x[j])
            print(pair)


# #Question:-8

print("--------------QUESTION:- 8-----------------")

even_list = []
odd_list = []

while True:

    user_input8 = int(input("Please enter any number between 1 to 50: "))

    if user_input8 % 2 == 0:
        if len(even_list) == 5:
            pass
        else:
            even_list.append(user_input8)

    else:
        if len(odd_list) == 5:
            pass
        else:
            odd_list.append(user_input8)
    
    if len(even_list) == 5 and len(odd_list) == 5:
        break

sum_even = 0
sum_odd = 0

for i in even_list:
    sum_even = sum_even + i

for i in odd_list:
    sum_odd = sum_odd + i

print(max(sum_even, sum_odd)) 


# #Question:-9

print("--------------QUESTION:- 9-----------------")

user_input9 = list(input("Enter the string: "))

string1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

result = []

for i in string1:
    if i not in result:
        result.append(i)

        count = 0

        for j in range(len(user_input9)):
            if i == user_input9[j]:
                count += 1

        if count != 0:
            print("{} {}".format(i, count))

# #Question:-10

print("--------------QUESTION:- 10-----------------")

tuple_10 = (1,2,3,4,5,6,7,8,9,10)

result = tuple(i for i in tuple_10 if i % 2 == 0)

print(result)
