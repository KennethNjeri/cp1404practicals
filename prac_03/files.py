# question 1
out_file = open("names.txt","w")
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

#question 2
in_file = open("names.txt","r")
name = in_file.read()
in_file.close()
print(f"Hi {name}")

#question 3
with open("numbers.txt","r") as in_file:
    first_number = int(in_file.readline().strip())
    second_number = int(in_file.readline().strip())

total = first_number + second_number
print(total)

#question 4
total = 0
with open("numbers.txt","r") as in_file:
    for line in in_file:
        number = int(line.strip())

total += number
print(total)
