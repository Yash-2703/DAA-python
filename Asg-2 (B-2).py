'''---------------------------------------------------------------------------------------------------------------------------------------------
Problem Statement : Implement a problem of maximize Profit by trading stocks based on given rate per day.
                    -Given an array arr[] of N positive integers which denotes the cost of selling and buying a stock on
                     each of the N days. The task is to find the maximum profit that can be earned by buying a stock on or selling
                     all previously bought stocks on a particular day.
---------------------------------------------------------------------------------------------------------------------------------------------'''


def max_profit(prices):
    n = len(prices)
    profit = 0
    buy = prices[0]  # Initialize buy price to the first day's price

    for i in range(1, n):
        if prices[i] > prices[i - 1]:
            # If the price is increasing, sell the stock at the current day
            profit += prices[i] - buy
        buy = prices[i]  # Update the buy price for the next day

    return profit

# Example usage:
prices = [100, 180, 260, 310, 40, 535, 695]
max_profit_value = max_profit(prices)
print("Maximum Profit:", max_profit_value)