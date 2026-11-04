# Stock Profit Calculator
# My first Python project

buy_price = float(input("Enter buying price: "))
sell_price = float(input("Enter selling price: "))

profit = sell_price - buy_price
return_percent = (profit / buy_price) * 100

print("Buying Price:", buy_price)
print("Selling Price:", sell_price)
print("Profit:", profit)
print("Return:", return_percent, "%")

if profit > 0:
    print("You made a profit!")
elif profit < 0:
    print("You made a loss!")
else:
    print("No profit, no loss!")
