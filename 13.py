from typing import List, Any
def print_only_5_multipliers(data:List[Any]):
    only_fives =[value for value in data if not value % 5]
    print(only_fives)

num_list = [10, 20, 33, 46, 55]
print(print_only_5_multipliers(num_list))