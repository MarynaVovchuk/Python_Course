
def sum():
    a = int(input())
    if a != 0:
        a = a + sum()
    return a

print(sum())
