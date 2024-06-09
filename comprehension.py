products = ["t-shirt", "mug", "hat", "book", "keychain"]
inventory = {}
customer_orders = set()
def initialize_inventory(products_list):
  
  inventory = {item:int(input(f"How many {item}s are there in the inventory?")) for item in products_list}
  return inventory

def get_customer_orders():


    number_of_orders = int(input("How many items would you like to order?"))
    customer_orders = {input(f"what is the #{order_counter+1} order? ") for order_counter in range(number_of_orders)}
    return customer_orders

def calculate_order_statistics(inventory, customers_orders):
    total_products_ordered = len(customer_orders)
    total_products = sum(inventory.values())
    percentage_of_products_ordered = round(total_products_ordered / total_products , 2)
    order_stat = (total_products_ordered, percentage_of_products_ordered)
    return order_stat

def update_inventory(inventory, customers_orders):
   updated_inventory = {key:(value-1 if key in customers_orders else value) for (key,value) in inventory.items()}
   updated_inventory = {key:value for (key,value) in updated_inventory.items() if updated_inventory[key] >0}
   return updated_inventory


def print_order_statistics(order_stat):
    print("Order Statistics:")
    print(f"Total Products Ordered: {order_stat[0]}")
    print(f"Percentage of Products Ordered: {order_stat[1] * 100}%")

def print_updated_inventory(inventory):
    output = '\n'.join(f"{product}:{quantity}" for product,quantity in inventory.items() )
    print("Updated inventory has:",'\n' ,output)

def calculate_total_price(customer_orders):
    prices = [int(input(f"what's the price of a {item}?")) for item in customer_orders]
    total_price = sum(prices)
    print(f"Total price is: {total_price}")


inventory = initialize_inventory(products)
customer_orders = get_customer_orders()
order_statistic = calculate_order_statistics(inventory, customer_orders)
print_order_statistics(order_statistic)
inventory = update_inventory(inventory,customer_orders)
print_updated_inventory(inventory)
calculate_total_price(customer_orders)


