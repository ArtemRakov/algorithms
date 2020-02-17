def solve(attr):
    number, power = attr
    res = 1
    for _ in range(1, power + 1):
        res *= number
    return res

