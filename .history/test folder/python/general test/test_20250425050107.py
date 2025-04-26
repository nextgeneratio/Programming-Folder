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
    
