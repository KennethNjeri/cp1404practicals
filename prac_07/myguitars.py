from prac_07.guitar import Guitar


def main():
    guitars = []
    in_file = open("guitars.csv", "r")
    for line in in_file:
        parts = line.strip().split(",")
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    add_new_guitars(guitars)

    save_new_guitars(guitars, "guitars.csv")

    guitars.sort()
    for guitar in guitars:
        print(guitar)


def add_new_guitars(guitars):
    print("Enter new guitars")
    name = input("Name: ")
    while name != "":
        year = input("Year: ")
        cost = input("Cost: ")
        guitars.append(Guitar(name, int(year), float(cost)))
        name = input("Name: ")


def save_new_guitars(guitars, filename):
    out_file = open(filename, "w")
    for guitar in guitars:
        out_file.write(f'{guitar.name},{guitar.year},{guitar.cost}\n')
    out_file.close()


if __name__ == "__main__":
    main()
