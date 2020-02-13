def solve(res):
    u, v = res
    if u == v:
        return u

    if u == 0:
        return v

    if v == 0:
        return u


    # u is even
    if u & 1 == 0:
        # v is even
        if v & 1 == 0:
            # 2 * gcd(u/2, v/2)
            return 2*solve([u >> 1, v >> 1])
        # v is odd
        else:
            # gcd(u / 2, v)
            return solve([u >> 1, v])
    # u is odd
    else:
        # v is even
        if v & 1 == 0:
            return solve([u, v >> 1])
        # v is odd and u is greater than v
        elif u > v and v & 1 != 0:
            return solve([(u-v) >> 1, v])
        # v is odd and u is smaller than v
        else:
            return solve([(v-u) >> 1, u])
