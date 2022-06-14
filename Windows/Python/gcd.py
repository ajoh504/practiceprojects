#! python3
# gcd.py - find the greatest common divisor of two numbers

def gcd(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a = a - b
            gcd = [a, b]
        elif b > a:
            b = b - a
            gcd = [a, b]
    return a
