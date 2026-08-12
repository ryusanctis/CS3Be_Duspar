#Mars = 0.38 Jupiter = 2.34 Moon = 0.1


def calculate_space_weight(earth_weight, destination):
    if destination == "Mars":
        earth_weight = earth_weight * 0.38
        return earth_weight
    elif destination == "Jupiter":
        earth_weight = earth_weight * 2.34
        return earth_weight
    elif destination == "Moon":
        earth_weight = earth_weight * 0.1
        return earth_weight
    else:
        print("Invalid destination. Please try again.")
        print("Remember that the only valid inputs are either 'Mars', 'Jupiter', or 'Moon'.")

        
def main():
    print("Welcome, astronaut, to the space weight calculator of the Philippine Space Agency.")
    print("Please enter your inputs properly to avoid any errors that may occur.")
    earth_weight = float(input("What is your weight on Earth in kg?"))
    destination = input("What is your destination? (Mars, Jupiter, Moon)")
    calculate_space_weight(earth_weight, destination)
    print("Your weight on your planned destination is: ", calculate_space_weight(earth_weight, destination), "kg.")

main()

