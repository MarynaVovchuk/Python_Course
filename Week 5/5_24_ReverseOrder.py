
myList = list(map(int, input().split()))

for i in range(len(myList) - 1, -1, -1):
    print(myList[i], end=' ')
