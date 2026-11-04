# Stock Profit and Loss Calculator
# Project 1 - Python Fundamentals
# Learning Quantitative Finance

def stock_calculator(buy, sell):

    # Validate buying price
    if buy <= 0:
        print("Buying price must be greater than zero!")
        return

    # Calculate profit or loss
    profit = sell - buy

    # Calculate percentage return
    return_percent = (profit / buy) * 100

    return profit, return_percent


# Get input from user
buy = float(input("Enter buying price: "))
sell = float(input("Enter selling price: "))

# Run stock calculator
result = stock_calculator(buy, sell)

# Display results
if result is not None:
    profit, percentage = result

    print("Profit/Loss:", profit)
    print("Return:", percentage, "%")
