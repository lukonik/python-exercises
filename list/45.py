def get_power_set(lst):
    result = [[]]
    for element in lst:
        # For every existing subset, create a new one including the 'element'
        new_subsets = [subset + [element] for subset in result]
        result.extend(new_subsets)
    return result


# Test the function
base_list = [1, 2, 3]
subsets = get_power_set(base_list)

print(f"Original: {base_list}")
print(f"Power Set (Count {len(subsets)}): {subsets}")
