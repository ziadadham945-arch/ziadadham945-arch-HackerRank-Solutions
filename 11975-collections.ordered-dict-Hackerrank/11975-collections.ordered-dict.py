from collections import OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    item_data = input().rsplit(' ', 1)
    name = item_data[0]
    price = int(item_data[1])
    
    items[name] = items.get(name, 0) + price

for name, total_price in items.items():
    print(f"{name} {total_price}")


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna