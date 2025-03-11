def nested_sum(lst):
    total = 0
    for element in lst:
        if isinstance(element, list):
            total += nested_sum(element)
        else:
            total += element
    return total


numbers = [1, 3, 5, 6, [7, 8]]
print(nested_sum(numbers))  



def find_min_max(nested_list):
    min_val = float('inf')
    max_val = float('-inf')

    for element in nested_list:
        if isinstance(element, list):
            sub_min, sub_max = find_min_max(element)
            min_val = min(min_val, sub_min)
            max_val = max(max_val, sub_max)
        else:
            min_val = min(min_val, element)
            max_val = max(max_val, element)

    return min_val, max_val

# Example usage
nested_list = [1, 3, [5, 6, [7, 8]], 2, [4, [9, 0]]]
minimum, maximum = find_min_max(nested_list)
print(f"Minimum value: {minimum}")  # Output: Minimum value: 0
print(f"Maximum value: {maximum}")  # Output: Maximum value: 9

