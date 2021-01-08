
def gcd(a, b):
    if b == 0:
        return a
    if a % b == 0:
        return b
    return gcd(b, a % b)


def ReduceFraction(n, m):
    return int(n / gcd(n, m)), int(m / gcd(n, m))

n = int(input())
m = int(input())

print(*ReduceFraction(n, m))
