try:
    charge_for_just_food = float(input("Please enter how much you were charged for the food in dollars: $"))
    if charge_for_just_food < 0:
        raise ValueError
except ValueError:
    print("Error: Please enter a positive numeric float (decimal) value for the food charge.")
    exit()

tip_charge = charge_for_just_food * 0.18
tax_charge = charge_for_just_food * 0.07
total_charge = charge_for_just_food + tip_charge + tax_charge

print("Food charge: ${:.2f}".format(charge_for_just_food))
print("Tip (18%): ${:.2f}".format(tip_charge))
print("Sales tax (7%): ${:.2f}".format(tax_charge))
print("Total price: ${:.2f}".format(total_charge))
