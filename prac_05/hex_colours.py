NAME_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Alice Blue": "#f0f8ff", "Aliriza Crimson": "#e32636",
"Amaranth": "#e52b50", "Amber": "#ffbf00","Amethyst": "#9966cc","Antique White": "#faebd7", "Antique White1": "#ffefdb",
"Antique White2": "#eedfcc","Antique White3": "#cdc0b0"}

color_name = input("Enter a color name: ").title()
while color_name != "":
    try:
        print(NAME_TO_CODE[color_name])
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter a color name: ").title()
