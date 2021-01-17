
import math


def sums(n, cur_sum, a):
    a = a or []
    if len(a) > 4:
        return
    if cur_sum == n:
        return a
    for i in range(int(math.sqrt(n - cur_sum)), 0, -1):
        res = sums(n, cur_sum + i ** 2, a + [i])
        if res:
            return res

print(*sums(int(input()), 0, None))
