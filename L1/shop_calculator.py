total_price = 0
item_number = int(input('Enter the number of items:'))
while item_number < 0:
    print('Invalid')
    item_number = int(input('Enter the number of items:'))

for i in range(item_number):
    item_price = float(input('Enter the price of the item:'))
    total_price += item_price

if total_price >= 100:
    total_price = total_price * 0.9

print("Total price for {} items is ${:.2f}".format(item_number, total_price))
