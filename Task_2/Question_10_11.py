
#Question:- 10

print("--------------QUESTION:- 10-----------------")
correct_number = 100
counter = 0
while counter < 5:
    guess_number = int(input("Enter the number:- "))
    if(guess_number != correct_number):
        if(counter == 4):
            print("Game Over!")
        else:
            print("Try again!")
    else:
        print("Good guess!")
        if(counter == 4):
            print("Game Over!")
    counter += 1


#Question:- 11

print("--------------QUESTION:- 11-----------------")
correct_number = 100
counter = 0
while counter < 5:
    guess_number = int(input("Enter the number:- "))
    if(guess_number != correct_number):
        if(counter == 4):
            print("Sorry but that was not very successful")
        else:
            print("Try again!")
    else:
        print("Good guess!")
        break
    counter += 1
