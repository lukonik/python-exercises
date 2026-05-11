def is_prime(value: int):
    if value < 2:
        return True

    for item in range(2, value):
        if value % item == 0:
            return False

    return True


def generate_primes(start: int, end: int):
    return [value for value in range(start, end) if is_prime(value)]


print(generate_primes(10, 50))
