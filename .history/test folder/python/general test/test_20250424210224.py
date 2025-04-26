def max_profit(prices):
    """
    Calculate the maximum profit by buying and selling stocks multiple times.
    
    :param prices: List[int] - List of stock prices
    :return: int - Maximum profit
    """
    if not prices or len(prices) < 2:
        return 0

    max_profit = 0

    # Iterate through the prices and add the profit for every upward trend
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]

    return max_profit


# Test cases
print(max_profit([7, 1, 5, 3, 6, 4]))  # Expected output: 7 (buy at 1, sell at 5, buy at 3, sell at 6)
print(max_profit([7, 6, 4, 3, 1]))     # Expected output: 0 (no profit possible)
