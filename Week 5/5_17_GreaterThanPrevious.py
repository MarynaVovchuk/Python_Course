
myList = list(map(int, input().split()))

for i in range(len(myList) - 1):
    if myList[i] < myList[i + 1]:
        print(myList[i + 1], end=' ')
