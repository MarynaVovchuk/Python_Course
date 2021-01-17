
def findSquares():
    a = int(input())
    if a == 0:
        return
    findSquares()
    if a ** (1 / 2) % 1 == 0:
        print(a)

findSquares()
