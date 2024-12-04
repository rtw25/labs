from typing import List, Any

def zipmap(key_list: List[Any], value_list: List[Any], override: bool = False) -> dict:
    if not override and len(set(key_list)) != len(key_list):
        return {}
    # Extend the value_list with None if key_list is longer
    value_list = value_list + [None] * (len(key_list) - len(value_list))
    # Use map and zip to create the dictionary
    return dict(map(lambda kv: kv, zip(key_list, value_list)))

# Examples
print(zipmap(['a', 'b', 'c', 'd'], [1, 2, 3, 4]))  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(zipmap([1, 2, 3, 2], [4, 5, 6, 7], True))    # {1: 4, 2: 7, 3: 6}
print(zipmap([1, 2, 3], [4, 5, 6, 7, 8]))         # {1: 4, 2: 5, 3: 6}
print(zipmap([1, 3, 5, 7], [2, 4, 6]))            # {1: 2, 3: 4, 5: 6, 7: None}
