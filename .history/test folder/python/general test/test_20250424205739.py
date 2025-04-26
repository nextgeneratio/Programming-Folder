def max_profit(prices):
    """
    This function takes a list of prices and returns the maximum profit that can be made by buying and selling once.
    :param prices: List of prices
    :return: Maximum profit
    """
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


