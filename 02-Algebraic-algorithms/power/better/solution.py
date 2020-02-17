def solve(attr):
    number, power = attr
    base = number
    res = 1
    while power != 0:
        if power % 2 == 0:
            power /= 2
            base *= base
        else:
            power -= 1
            res *= base
    return res

