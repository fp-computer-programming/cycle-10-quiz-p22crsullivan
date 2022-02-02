from hashlib import new


prices = [30, 40, 25, 55, 60, 80, 65]
sales = [1, 3, 2, 5, 2, 1, 2]
items = [['tee-shirt','long-sleeved','tanktop'],['quarter-zip','pullover','full-zip', 'half-zip']]

# Question 1
# Define average_price function
def average_price(prices):
# Create for loop to check prices list
    for index, value in prices:
        total_value = prices[value]
        total_index = prices[index]
        new_prices = total_value / total_index
# Return the value
    return new_prices
# Test the function
print(average_price([30, 40, 25, 55, 60, 80, 65]))

# Question 2
# Define price_changer function
def price_changer(prices):
# Create for loop to subtract 5 from each price
    for index, value in prices:
        remade_prices = []
        final_remade_prices = remade_prices[value] - 5
# Return the value
    return final_remade_prices
# Test the function
print(price_changer([30, 40, 25, 55, 60, 80, 65]))

# Question 3
# Define earnings function
def earnings(prices, sales):
# Create first for loop for prices
    for index, value in prices:
        price = value
        return price
# Create second for loop for sales
    for index2, value2 in sales:
        sale = value2
        return sale
# Test the function
print(earnings([30, 40, 25, 55, 60, 80, 65], [1, 3, 2, 5, 2, 1, 2]))

# Question 4
# Define earnings function
def new_prices(prices):
# Create for loop to check if item is greater than 40
    for index, value in prices:
        if value > 40:
            new_value = value - 10
            return new_value
# Test the function
print(new_prices([30, 40, 25, 55, 60, 80, 65]))

# Question 5
# Define item_costs function
def item_costs(prices, items):
    for index, value in prices:
