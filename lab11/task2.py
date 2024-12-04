from typing import Callable, List, Any, Dict

def group_by(f: Callable[[Any], Any], target_list: List[Any]) -> Dict[Any, List[Any]]:
    result = {}
    for item in target_list:
        key = f(item)
        result.setdefault(key, []).append(item)
    return result

# Examples
print(group_by(len, ["hi", "dog", "me", "bad", "good"]))
# {2: ["hi", "me"], 3: ["dog", "bad"], 4: ["good"]}
