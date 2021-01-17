
n, k = map(int, input().split())
myList = list('I' * n)

for i in range(k):
    l, r = map(int, input().split())
    for j in range(l, r + 1):
        myList.insert(j, '.')
        myList.pop(j - 1)

print(*myList, sep='')
