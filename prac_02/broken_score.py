"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))
    result = calculate_result(score)
    print(result)
    random_score = random.randint(1, 100)
    result = calculate_result(random_score)
    print(result)
    
def calculate_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "bad"


main()
