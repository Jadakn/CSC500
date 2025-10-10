try:
    food_charge = float(input("Enter how much you were charged for the food in dollars: $"))
    if food_charge < 0:
        raise ValueError
except ValueError:
    print("Error: Please enter a positive numeric float (decimal) value for the food charge.")
    exit()
tip = food_charge * 0.18
tax = food_charge * 0.07
total = food_charge + tip + tax
print(f"Food charge: ${food_charge:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Sales tax (7%): ${tax:.2f}")
print(f"Total price: ${total:.2f}")
