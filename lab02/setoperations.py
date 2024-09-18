
def make_set(data):
    data = data.split(",")
    data = [int(item.strip()) for item in data]
    unique_list = []
    for item in data:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

data = input("input a list of numbers separated by commas: ")
unique_list = make_set(data)
print("the set is:", unique_list)

def is_set(data):
    if data is None:
        return False
    seen_elements = []
    for item in data:
        if item in seen_elements:
            return False
        else:
            seen_elements.append(item)
    return True
input_list = [int(item.strip()) for item in data.split(",")]
result = is_set(input_list)
print("the data is a set:", result)

def union(setA, setB):
    if not is_set(setA) or not is_set(setB):
        return []

    union_set = []
    for item in setA:
        if item not in union_set:
            union_set.append(item)
    for item in setB:
        if item not in union_set:
            union_set.append(item)

    return union_set

def intersection(setA, setB):
    if not is_set(setA) or not is_set(setB):
        return []

    intersection_set = []
    for item in setA:
        if item in setB and item not in intersection_set:
            intersection_set.append(item)

    return intersection_set
input_string_A = input("Input the first list of numbers separated by commas for set A: ")
input_string_B = input("Input the second list of numbers separated by commas for set B: ")
setA = make_set(input_string_A)
setB = make_set(input_string_B)

result_union = union(setA, setB)
result_intersection = intersection(setA, setB)

print("Union of set A and set B:", result_union)
print("Intersection of set A and set B:", result_intersection)
