def remove_match_char(list1, list2):
    """
    Remove elements from list1 that are present in list2.
    
    Args:
        list1 (list): The first list from which to remove elements.
        list2 (list): The second list containing elements to remove from list1.
    
    Returns:
        list: A new list with elements from list1 that are not in list2.
    """
    return len([item for item in list1 if item not in list2])

def create_list():
    name = input("Enter a name: ")
    # Remove spaces and convert to a list of characters
    result = list(name.replace(" ", "")).lower()
    return result


def main():
    char_rep = {
        "F": "Friends",
        "L": "Love",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemy",
        "S": "Siblings"
    }

    print("Player 1, please enter your name:")
    player1 = create_list()
    print("Player 2, please enter your name:")
    player2 = create_list()

    # Calculate the count of unmatched characters
    count = remove_match_char(player1, player2)

    # FLAMES algorithm
    flames = list(char_rep.keys())
    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            # Remove the character at split_index and rotate the list
            flames = flames[split_index + 1:] + flames[:split_index]
        else:
            # Remove the last character
            flames.pop()

    # The last remaining character determines the relationship
    result = char_rep[flames[0]]
    print(f"The relationship is: {result}")

main()
