# #Question:-1

# print("--------------QUESTION:- 1-----------------")
# while True:
#     try:
#         print('Hello World)
#     except SyntaxError:
#         print("Check your syntex")


#Question:-2

print("--------------QUESTION:- 2-----------------")

try:
    path = 'test.txt'
    f = open(path, 'r')
except FileNotFoundError as err:
    print("there is no file with name", path)
else:
    f.close()


#Question:-3

print("--------------QUESTION:- 3-----------------")

while True:
  try:
    user_input = input("Enter any four digit number:- ")
    if len(user_input) != 4:
      raise ValueError("The length is too short/long")
    break
  except ValueError as ve:
    print(ve)


#Question:-4

print("--------------QUESTION:- 4-----------------")

count = 0

while count < 3:
  username = input("Enter Username: ")
  password = input("Enter Password: ")
  if username == "admin" and password == "password":
    print("Login Successful!")
    break
  else:
    print("Try Again!")
    count += 1


# Question:-5

print("--------------QUESTION:- 5-----------------")
with open("doc.txt") as f:
  data = f.readlines() 
  for line in data: 
    words = line.split() 
    for word in words:
      if len(word) % 2 == 0:
        print(word)
