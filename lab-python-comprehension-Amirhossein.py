products = ["t-shirt", "mug", "hat", "book", "keychain"]
inventory = {}
customer_orders = set()
def initialize_inventory(products_list):
  for item in products_list:
    inventory[item]= int(input(f"How many {item}s are there in the inventory?"))
  return inventory

def get_customer_orders():

    continue_ordering = True
    while continue_ordering:
        customer_orders.add((input(f"what is your order? ")))
        next_order = input(f"Was that all?(yes/no)")
        if next_order == 'yes':
            continue_ordering = False
    return customer_orders

def calculate_order_statistics(inventory, customers_orders):
    total_products_ordered = len(customer_orders)
    total_products = sum(inventory.values())
    percentage_of_products_ordered = round(total_products_ordered / total_products , 2)
    order_stat = (total_products_ordered, percentage_of_products_ordered)
    return order_stat

def update_inventory(inventory, customers_orders):
   for product in customer_orders:
      inventory[product] -= 1

def print_order_statistics(order_stat):
    print("Order Statistics:")
    print(f"Total Products Ordered: {order_stat[0]}")
    print(f"Percentage of Products Ordered: {order_stat[1] * 100}%")

def print_updated_inventory(inventory):
    print("Updated inventory has:")
    for product,quantity in inventory.items():
        print(f"{product}:{quantity}")



initialize_inventory(products)
customer_orders = get_customer_orders()
order_statistic = calculate_order_statistics(inventory, customer_orders)
print_order_statistics(order_statistic)
update_inventory(inventory,customer_orders)
print_updated_inventory(inventory)


