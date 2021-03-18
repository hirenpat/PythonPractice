
# #Question:-1

print("--------------QUESTION:- 1-----------------")

import math

user_input1 = input("Please enter D: ")
user_input1 = user_input1.split(',')

result = []

for num in user_input1:
    Q = round(math.sqrt(2*50*int(num) / 30))
    result.append(Q)

print(result)

# #Question:-2

print("--------------QUESTION:- 2-----------------")

class Shape():
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.length = length
    
    def area(self):
        return self.length*self.length

bread = Square(3)
print(bread.area())

# #Question:-3

print("--------------QUESTION:- 3-----------------")

class FindTriple:
    def findTriple(self, arr):
        n = len(arr)
        found = False

        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if(arr[i] + arr[j] + arr[k] == 0):
                        print(arr[i], arr[j], arr[k])
                        found = True

result = FindTriple()
result.findTriple([-25, -10, -7, -3, 2,4, 8, 10])

# #Question:-4

print("--------------QUESTION:- 4-----------------")

class Time():
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def addTime(t1, t2):
        totalTime = Time(0,0)

        totalTime.hours = t1.hours + t2.hours
        totalTime.minutes = t1.minutes + t2.minutes

        while totalTime.minutes >= 60:
            totalTime.hours += 1
            totalTime.minutes -= 60

        return totalTime
    
    def displayTime(self):
        print("The total time is ", self.hours,"hours and ", self.minutes, "minutes.")
    
    def displayMinute(self):
        print("The total minutes is ", (self.hours * 60) + self.minutes)

test1 = Time(2,50)
test2 = Time(1,20)
result = Time.addTime(test1, test2)

result.displayTime()
result.displayMinute()


# #Question:-5

print("--------------QUESTION:- 5-----------------")

class Person():
    age = 0

    def __init__(self, initial_age):
        if initial_age < 0:
            print("Age is not valid")
            self.age = 0
        else:
            self.age = initial_age
    
    def amIOld(self):
        if self.age < 13:
            print("You're young")
        elif self.age >= 13 and self.age <18:
            print("You're a teenager")
        else:
            print("You're old")
    
    def yearPasses(self):
        self.age += 1

hiren = Person(20)
hiren.amIOld()

random = Person(-1)
random.amIOld()

random1 = Person(15)
random1.amIOld()
random1.yearPasses()
