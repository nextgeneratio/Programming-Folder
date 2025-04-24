row = "|  " + " 0 " * 4 + "  |"
for _ in range(4):
    print(row)

def num_positioning(num, row, col):
    """
    Function to position a number in a 4x4 grid.
    :param num: The number to be positioned.
    :param row: The row index (0-3).
    :param col: The column index (0-3).
    :return: A string representing the formatted number in the grid.
    """
    return f"| {num} " + "  " * (col - 1) + " |" + "  " * (3 - col) + "  |" if col > 0 else f"| {num} " + "  " * (3 - col) + "  |"


print(num_positioning(1, 0, 0))  # Example usage
