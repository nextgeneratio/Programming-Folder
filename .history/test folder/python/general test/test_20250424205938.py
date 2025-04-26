def max_profit(prices):

    if not prices:
        return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


# Test cases
print(max_profit([7, 1, 5, 3, 6, 4]))  # Expected output: 5 (buy at 1 and sell at 6)
print(max_profit([7, 6, 4, 3, 1]))     # Expected output: 0 (no profit possible)
