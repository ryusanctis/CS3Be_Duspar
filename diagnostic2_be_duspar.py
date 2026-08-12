base_price = 10.00
pepperoni = 1.50
mushrooms = 1.50
extra_cheese = 1.50
toppings = ()

def calculate_total(topping_count):
    total = base_price + (topping_count * 1.50)
    return total

def main():
    print("Welcome to the Silver Pizza Parlor in PSHS-WVCIC Cooperative!")
    print("The prices for our items can be found below:"
          "\nBase Price: $10.00"
          "\nPepperoni: $1.50"
          "\nMushrooms: $1.50"
          "\nExtra Cheese: $1.50"
          )
    topping_count = 0
    while True:
        print("Please enter the toppings you would like to add to your pizza. Please enter done when you are finished.")
        toppings = input("Toppings: ")
        if toppings == "Pepperoni" or toppings == "Mushrooms" or toppings == "Extra Cheese":
            print("You have added", toppings, "to your pizza.")
            topping_count += 1
        elif toppings == "done":
            break
        else:
            print("That is an invalid topping, please try again."
                  "\nPlease remember that the only valid inputs are either 'Pepperoni', 'Mushrooms', or 'Extra Cheese', and 'done' if you are finished ordering.")
        calculate_total(topping_count)
    discount = input("Do you have a discount code?")
    if discount == "PYTHON20":
        print("You have a 20% discount on your current purchase!")
        print("Your total is: $", calculate_total(topping_count) * 0.8)
    else:
        print("Your total is: $", calculate_total(topping_count))
    print("Please pay at the counter to complete your order.")
    print("Thank you for ordering from the Silver Pizza Parlor, we hope to see your continued patronage in the future!")

main()