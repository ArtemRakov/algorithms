def solve(attr):
    number, power = attr
    res = 1
    base = number

    while power > 0:
        if power % 2 == 1:
            res *= base

        base *= base
        power = power // 2

    return res

