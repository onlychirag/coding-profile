import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_factors(n):
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n = n // 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            prime_factors.append(i)
            n = n // i
    if n > 2:
        prime_factors.append(n)
    return prime_factors

def smallest_value(n):
    while not is_prime(n):
        prime_factors = find_prime_factors(n)
        n = sum(prime_factors)
    return n
print(smallest_value(15))