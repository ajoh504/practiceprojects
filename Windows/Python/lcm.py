#!python3
# lcm.py - find the least common multiple of two numbers

def lcm(a: int, b: int) -> int:
    i = 1
    multiples_of_a = []
    multiples_of_b = []
    while True:
        multiples_of_a.append(a * i)
        multiples_of_b.append(b * i)
        i += 1
        for match_a in multiples_of_a:
            if match_a in multiples_of_b:
                return match_a
        for match_b in multiples_of_b:
            if match_b in multiples_of_a:
                return match_b
