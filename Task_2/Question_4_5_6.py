
#Question:- 4

print("--------------QUESTION:- 4-----------------")

user_input = int(input("Enter any value:- "))
while(user_input):
    
    if(user_input >= 0):
        print("Good Going!")
        user_input = int(input("Enter any value:- "))
        continue
    else:
        print("It's over!")
        break


#Question:- 5

print("--------------QUESTION:- 5-----------------")
num = 2000
while(num >= 2000 and num <= 3200):
    if(num % 7 == 0):
        if(num % 5 != 0):
            print(num)
    num += 1 


#Question:- 6

print("--------------QUESTION:- 6-----------------")
# x = 123
# for i in x:
#     print(i)
# 'int' object is not iterable

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print("error")
# 0
# error
# 1
# error
# 2

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# 0
# 1
# 2
# 3
# 4
