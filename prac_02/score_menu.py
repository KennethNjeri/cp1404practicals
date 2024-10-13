MENU = """(G)-Get a valid score 
(P)-Print result 
(S)-Show stars 
(Q)-Quit"""
print(MENU)


def main():
    score = get_valid_score()
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = calculate_result(score)
            print(result)
        elif choice == "S":
            stars = show_stars(score)
            print(stars)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Choice: ")
    print("Farewell")


def get_valid_score():
    score = int(input("Enter your score: "))
    while score < 0 or score > 100:
        print("Score must be between 0 and 100")
        score = int(input("Enter your score: "))
    return score

def calculate_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    stars = "*" * score
    return stars

main()