DISCOUNT_RATE = 0.1

number_of_items = int(input("Number of items: "))
total_price = 0
while number_of_items <= 0:
    print("Invalid number_of_items.")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price
    if total_price > 100:
        discount_price = total_price * DISCOUNT_RATE
        total_price = total_price - discount_price
print(f"Total price for {number_of_items} items is {total_price:.2f}")