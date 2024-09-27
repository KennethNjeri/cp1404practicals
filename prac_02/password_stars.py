minimum_length = 6

password = input("Enter a password: ")
while len(password) < minimum_length:
    print("Invalid password")
    password = input("Enter a password: ")
print("*" * len(password))
