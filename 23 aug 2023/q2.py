
class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.table_reservations = []
        self.customer_orders = []
    def add_item_to_menu(self, item_name, price):
        self.menu_items[item_name] = price
    def book_table(self, table_number):
        self.table_reservations.append(table_number)
    def take_customer_order(self, table_number, order):
        self.customer_orders.append({"table_number": table_number, "order": order})
    def print_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price}")
    def print_table_reservations(self):
        print("Table Reservations:")
        print(self.table_reservations)
    def print_customer_orders(self):
        print("Customer Orders:")
        for order in self.customer_orders:
            print(f"Table {order['table_number']}: {order['order']}")

# Create an instance of the Restaurant class
restaurant = Restaurant()
# Add items to the menu
restaurant.add_item_to_menu("Burger", 100)
restaurant.add_item_to_menu("Pizza", 123)
restaurant.add_item_to_menu("Salad", 273)
# Book tables
restaurant.book_table(1)
restaurant.book_table(3)
# Take customer orders
restaurant.take_customer_order(1, ["Burger", "Fries"])
restaurant.take_customer_order(3, ["Pizza", "Coke"])
# Print menu, table reservations, and customer orders
restaurant.print_menu()
print()
restaurant.print_table_reservations()
print()
restaurant.print_customer_orders()

