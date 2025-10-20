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
    first_item_name = input("Enter the item name:\n")
    try:
        first_item_price = float(input("Enter the item price:\n"))
    except ValueError:
        print("Error: Please enter a valid float value for the item price.")
        exit()
    try:
        first_item_quantity = int(input("Enter the item quantity:\n"))
        if first_item_quantity < 0:
            raise ValueError
    except ValueError:
        print("Error: Please enter a valid positive integer value for the item quantity.")
        exit()
    first_item = ItemToPurchase(first_item_name, first_item_price, first_item_quantity)

    print("\nItem 2")
    second_item_name = input("Enter the item name:\n")
    try:
        second_item_price = float(input("Enter the item price:\n"))
    except ValueError:
        print("Error: Please enter a valid float value for the item price.")
        exit()
    try:
        second_item_quantity = int(input("Enter the item quantity:\n"))
        if second_item_quantity < 0:
            raise ValueError
    except ValueError:
        print("Error: Please enter a valid positive integer value for the item quantity.")
        exit()
    second_item = ItemToPurchase(second_item_name, second_item_price, second_item_quantity)

    print('')
    print("TOTAL COST")
    first_item.print_item_cost()
    second_item.print_item_cost()
    total_cost = first_item.item_price * first_item.item_quantity + second_item.item_price * second_item.item_quantity
    print("Total: $", format(total_cost, '.2f'))
