
numbers = []
for i in range(5):
    number = float(input("Enter a number: "))
    numbers.append(number)

# Output information about these numbers
print(f"The first number is:{numbers[0]}")
print(f"The last number is:{numbers[-1]}")
print(f"The smallest number is:{min(numbers)}")
print(f"The largest number is:{max(numbers)}")
print(f"The average of the numbers is: {sum(numbers)/len(numbers)}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

name = input("Enter your name: ")
if name in usernames:
    print(f"Access granted")
else:
    print(f"Access denied")