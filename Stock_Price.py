import random

min_price = 0.01 # minimum price
max_price = 100.00 # maximum price
max_increase = 0.175 # 17.5% increase
max_decrease = 0.05 # 5% decrease
init_price = 1.00 # day 1 price
print("Starting price", ("${:,.2f}").format(init_price))
while init_price >= min_price and init_price <= max_price:
    randomChange = 0
    if random.randint(1,2) == 1:
        priceChange = random.uniform(0.01,max_increase)
    else:
        priceChange = random.uniform(---max_decrease,0)
    init_price *= (priceChange + 1)
    print(("${:,.2f}").format(init_price))