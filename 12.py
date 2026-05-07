from typing import Dict, List


def reverse_dict(dict: Dict[str, List[str]]):
    return {item: key for key, value in dict.items() for item in value}


print(reverse_dict({"Orwell": ["1984", "Animal Farm"], "Huxley": ["Brave New World"]}))
