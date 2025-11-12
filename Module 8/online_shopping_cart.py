class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.description = "none"

    def __init__(self, item_name, item_price, item_quantity, description):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.description = description

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(self.item_name, self.item_quantity, "@ $", format(self.item_price, '.2f'), "= $", format(total_cost, '.2f'))

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, i):
        self.cart_items.append(i)

    def remove_item(self, i):
        for item in self.cart_items:
            if item.item_name == i:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, i):
        for item in self.cart_items:
            if item.item_name == i.item_name:
                if i.description != "none" and i.item_price != 0.0 and i.item_quantity != 0:
                    item.description = i.description
                    item.item_price = i.item_price
                    item.item_quantity = i.item_quantity
            return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        num_items = sum(i.item_quantity for i in self.cart_items)
        return num_items

    def get_cost_of_cart(self):
        cost_of_cart = sum(i.item_price * i.item_quantity for i in self.cart_items)
        return cost_of_cart

    def print_total(self):
        print(self.customer_name, "'s Shopping Cart - ", self.current_date, sep='')
        num_items = self.get_num_items_in_cart()
        print("Number of Items:", num_items)
        if num_items == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for i in self.cart_items:
                i.print_item_cost()
            total_cost = self.get_cost_of_cart()
            print("Total: $", format(total_cost, '.2f'))

    def print_descriptions(self):
        print(self.customer_name, "'s Shopping Cart - ", self.current_date, sep='')
        print("Item Descriptions")
        for i in self.cart_items:
            print(i.item_name, ":", i.description)

    def print_menu(cart):
        options = (
            "MENU\n"
            "a - Add item to cart\n"
            "r - Remove item from cart\n"
            "c - Change item quantity\n"
            "i - Output items' descriptions\n"
            "o - Output shopping cart\n"
            "q - Quit\n"
        )
        choice = ''
        while choice != 'q':
            print(options)
            choice = input("Choose an option:\n")
            if choice == 'a':
                try:
                    item_name = input("Enter the item name: ")
                    item_price = float(input("Enter the item price: "))
                    item_quantity = int(input("Enter the item quantity: "))
                    description = input("Enter the item description: ")
                except ValueError:
                    print("Error: Strings are required for description and item name. An integer value required for quantity. A float value is required for price.")
                    continue
                item_to_add = ItemToPurchase(item_name, item_price, item_quantity, description)
                cart.add_item(item_to_add)
            elif choice == 'r':
                item_name = input("Enter name of item to remove: ")
                cart.remove_item(item_name)
            elif choice == 'c':
                item_name = input("Enter the item name: ")
                try:
                    new_quantity = int(input("Enter the new quantity: "))
                except ValueError:
                    print("Error: Please enter a valid item name and quantity.")
                    continue
                modified_item = ItemToPurchase(item_name, 0.0, new_quantity, "none")
                for i in cart.cart_items:
                    if i.item_name == item_name:
                        modified_item = ItemToPurchase(item_name, i.item_price, new_quantity, i.description)
                        break
                cart.modify_item(modified_item)
            elif choice == 'i':
                cart.print_descriptions()
            elif choice == 'o':
                cart.print_total()
            elif choice != 'q':
                print("Invalid option, please select a valid menu option below.")

def add_item_to_cart_input():
    while True:
        try:
            item_name = input("Enter the item name: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            description = input("Enter the item description: ")
            break
        except ValueError:
            print("Error: String format is required for item name and description. An integer value required for quantity. A float value is required for price.")
            continue
    return ItemToPurchase(item_name, item_price, item_quantity, description)


if __name__ == "__main__":
    first_item = add_item_to_cart_input()
    second_item = add_item_to_cart_input()
    total_cost = first_item.item_price * first_item.item_quantity + second_item.item_price * second_item.item_quantity
    print("\nTOTAL COST")
    first_item.print_item_cost()
    second_item.print_item_cost()
    total_cost = first_item.item_price * first_item.item_quantity + second_item.item_price * second_item.item_quantity
    print("Total: $", format(total_cost, '.2f'))

    while True:
        try:
            customer_name = input("Enter customer name: ")
            break
        except ValueError:
            print("Error: Please enter a valid customer name.")
            continue
    while True:
        try:
            current_date = input("Enter today's date: ")
            break
        except ValueError:
            print("Error: Please enter a valid date.")
            continue
    print("Customer name:", customer_name)
    print("Today's date:", current_date)
            
    cart = ShoppingCart(customer_name, current_date)
    # cart.add_item(ItemToPurchase("Nike Romaleos", 189.0, 2, "Volt color, Weightlifting shoes"))
    # cart.add_item(ItemToPurchase("Chocolate Chips", 3.0, 5, "Semi-sweet"))
    # cart.add_item(ItemToPurchase("Powerbeats 2 Headphones", 128.0, 1, "Bluetooth headphones"))
    ShoppingCart.print_menu(cart)
    cart.print_total()
    cart.print_descriptions()
    