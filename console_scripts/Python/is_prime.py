#!python3
# is_prime.py - return True if number is prime, False if not

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True
