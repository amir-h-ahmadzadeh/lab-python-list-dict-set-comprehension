In this project, I updated the functions to make the process of handling customer orders more interactive and efficient. I used comprehensions to gather input and update the inventory, which streamlined the code and made it more Pythonic.

First, I modified the get_customer_orders function. I designed it to ask the user for the number of customer orders. Then, I used a loop to gather the product names from the user. I accomplished this using a list comprehension, making the process both efficient and readable.
In this function, I start by asking the user how many orders they want to place. Then, for each order, I prompt them to enter the product name and store these names in a list.

Adding a Function to Calculate Total Price
2. Calculate Total Price
Next, I created a new function, calculate_total_price, to compute the total price of the customer’s order. For each product in customer_orders, I prompt the user to enter the price. I again used a list comprehension to gather these prices and then summed them to get the total.

Updating the update_inventory Function
3. Remove Out-of-Stock Products
I also modified the update_inventory function to ensure that products are removed from the inventory if their quantity drops to zero after fulfilling the orders. I used a dictionary comprehension to filter out any products that have zero quantity.

Printing the Total Price
4. Display Total Price
Finally, I added a line to print the total price of the customer’s order. Here’s how I put it all together:







