from prac_06.guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

guitar = Guitar(name,year,cost)
other = Guitar("Another",2013, cost)
print(f"{guitar.name} get_age() - Expected {102}. Got {guitar.get_age()}")
print(f"{other.name} get_age() - Expected {11}. Got {other.get_age()}")
print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
print(f"{other.name} is_vintage() - Expected False. Got {other.is_vintage()}")