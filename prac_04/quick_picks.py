import random

MIN_NUM = 1
MAX_NUM = 45
NUMBERS_PER_PICK = 6


def main():
    number_of_picks = int(input("How many picks? "))
    for i in range(number_of_picks):
        quick_picks = []
        while len(quick_picks) < NUMBERS_PER_PICK:
            number = random.randint(MIN_NUM, MAX_NUM)
            if number not in quick_picks:
                quick_picks.append(number)
        quick_picks.sort()
        print(" ".join(f"{number:2}" for number in quick_picks))


main()
