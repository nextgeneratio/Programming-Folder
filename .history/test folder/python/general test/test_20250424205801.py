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


# Test cases
def test_max_profit():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5, "Test case 1 failed"
    assert max_profit([7, 6, 4, 3, 1]) == 0, "Test case 2 failed"
    assert max_profit([]) == 0, "Test case 3 failed"
    assert max_profit([1]) == 0, "Test case 4 failed"
    assert max_profit([1, 2]) == 1, "Test case 5 failed"
    assert max_profit([2, 1]) == 0, "Test case 6 failed"

    print("All test cases passed!")


