from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    current_taxi = None
    bill = 0.0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Lets drive")
    print("q)uit", "c)hoose taxi", "d)rive")
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi is not None:
                bill += drive_taxi(current_taxi)
                print(f"Bill to date: {bill:.2f}")
            else:
                print("You need to choose a taxi before you drive")
        else:
            print("Invalid choice")
    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now: ")
    for taxi in taxis:
        print(taxi)

def display_taxis(taxis):
    """Displays taxis"""
    for index, taxi in enumerate(taxis):
        print("Taxis available")
        print(f"{index})-{taxi}")

def choose_taxi(taxis):
    """Choose a taxi"""
    display_taxis(taxis)
    taxi_choice = int(input("Choose a taxi: "))
    if 0 <= taxi_choice < len(taxis):
        return taxis[taxi_choice]
    else:
        print("Invalid taxi choice")
        return None


def drive_taxi(current_taxi):
    """Drives a taxi a given distance"""
    distance = float(input("Distance: "))
    current_taxi.start_fare()
    current_taxi.drive_taxi(distance)
    trip_cost = current_taxi.get_fare
    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
    return trip_cost
