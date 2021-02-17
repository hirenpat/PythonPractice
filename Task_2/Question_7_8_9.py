
# Question: - 7

print("--------------QUESTION:- 7-----------------")
num = 0
while(num < 6):
    if(num == 3):
        num += 1
        continue
    else:
        print(num)
        num += 1

# Question: - 8

print("--------------QUESTION:- 8-----------------")
digit_count = 0
letter_count = 0
user_input1 = input("Enter the string:- ")

for char in user_input1:
    if char.isdigit():
        digit_count += 1
    else:
        letter_count += 1

print("Letters:- ", letter_count)
print("Digits:- ", digit_count)


# Question: - 9

print("--------------QUESTION:- 9-----------------")
correct_number = 100
guess_number = int(input("Guess the lucky number:- "))

while(guess_number != correct_number):
    answer = input("Do you want to guess again (yes/no)?")
    if answer == "no":
        break
    guess_number = int(input("Guess the lucky number:- "))
