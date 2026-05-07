from typing import List


def prime_numbers(value: int):
    prime_numbers = []
    for item in range(1, value):
        is_prime = True
        for i in range(2, item):
            if item % i == 0:
                is_prime = False
        if is_prime:
            prime_numbers.append(item)
    return [value for (index,value) in enumerate(prime_numbers) if index % 2 ==1]


print(prime_numbers(20))
