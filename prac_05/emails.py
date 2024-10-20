def main():
    EMAIL_TO_NAME = {}

    email = input('Enter your email: ')
    while email != "":
        name = extract_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n)").upper()
        if confirmation != "Y" and confirmation != "":
            name = input("Enter your name: ").title()
        EMAIL_TO_NAME[email] = name
    for email, name in EMAIL_TO_NAME.items():
        print(f"{name} ({email})")

def extract_name_from_email(email):
    part = email.split('@')[0]
    name = ' '.join(part.split('.')).title()
    return name

main()