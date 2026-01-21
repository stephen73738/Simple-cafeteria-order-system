orders = []

def place_order():
    item = input("Enter food item: ")
    quantity = input("Enter quantity: ")
    orders.append({"item": item, "quantity": quantity})
    print("Order placed")

def view_orders():
    if not orders:
        print("No orders placed")
    else:
        for order in orders:
            print(order["item"], "- Quantity:", order["quantity"])

def main():
    while True:
        print("1. Place Order")
        print("2. View Orders")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            place_order()
        elif choice == "2":
            view_orders()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
