def sort_dicts_by_key(dict_list, key, reverse=False):
    """
    Sorts a list of dictionaries by a given key.

    Parameters:
        dict_list (list): A list of dictionaries to sort.
        key (str): The key to sort by.
        reverse (bool): If True, sorts in descending order. Default is False (ascending).

    Returns:
        list: A new list of dictionaries sorted by the specified key.
    """
    try:
        return sorted(dict_list, key=lambda d: d.get(key, None), reverse=reverse)
    except TypeError:
        raise ValueError(f"Cannot sort by key '{key}' — values are not comparable.")

# Example usage:
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30}
]

sorted_people = sort_dicts_by_key(people, "age")
print(sorted_people)


def sort_dicts_by_key(dict_list, key):
    return sorted(dict_list, key=lambda x: x[key])
