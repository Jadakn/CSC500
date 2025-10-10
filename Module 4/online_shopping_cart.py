class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def __init__(self, item_name, item_price, item_quantity):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(self.item_name, self.item_quantity, "@ $", format(self.item_price, '.2f'), "= $", format(total_cost, '.2f'))

if __name__ == "__main__":
    print("Item 1")
    item1_name = input("Enter the item name:\n")
    try:
        item1_price = float(input("Enter the item price:\n"))
    except ValueError:
        print("Error: Please enter a valid float value for the item price.")
        exit()
    try:
        item1_quantity = int(input("Enter the item quantity:\n"))
        if item1_quantity < 0:
            raise ValueError
    except ValueError:
        print("Error: Please enter a valid positive integer value for the item quantity.")
        exit()
    item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)

    print("\nItem 2")
    item2_name = input("Enter the item name:\n")
    try:
        item2_price = float(input("Enter the item price:\n"))
    except ValueError:
        print("Error: Please enter a valid float value for the item price.")
        exit()
    try:
        item2_quantity = int(input("Enter the item quantity:\n"))
        if item2_quantity < 0:
            raise ValueError
    except ValueError:
        print("Error: Please enter a valid positive integer value for the item quantity.")
        exit()
    item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)

    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    total_cost = item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity
    print("Total: $", format(total_cost, '.2f'))
