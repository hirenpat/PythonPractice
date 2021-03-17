# #Question:-1

print("--------------QUESTION:- 1-----------------")

string_1 = str("HelloWorld")

list_1 = [char for char in string_1 if char.isupper()]

print(list_1)


# #Question:-2

print("--------------QUESTION:- 2-----------------")

students = ['Smit','Jaya','Rayyan']
subjects = ['CSE','Networking','Operating System']

result = {students[i]: subjects[i] for i in range(len(students))}

print(result)


# #Question:-4

print("--------------QUESTION:- 4-----------------")

def rev_str(string_3):
    
    for i in range(len(string_3) - 1, -1, -1):
        yield string_3[i]

result = []
for char in rev_str("Consultadd Training"):
    result.append(char)
print(result)


# #Question:-5

print("--------------QUESTION:- 5-----------------")

def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

def display():
    print('display function ran')

decorator_display = decorator_function(display)

decorator_display()
