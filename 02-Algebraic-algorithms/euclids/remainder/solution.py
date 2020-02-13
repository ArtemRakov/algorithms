def solve(res):
    a, b = res
    if b == 0:
       return a
    return solve([b, a % b])

