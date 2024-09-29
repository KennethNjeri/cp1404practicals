
def main():
    minimum_length = 6
    get_password(minimum_length)


def get_password(minimum_length):
    password = input("Enter a password: ")
    while len(password) < minimum_length:
        print("Invalid password")
        password = input("Enter a password: ")
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


main()