
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)


def C(n, k):
    return fact(n) / (fact(n - k) * fact(k))

n = int(input())
k = int(input())

print(int(C(n, k)))
