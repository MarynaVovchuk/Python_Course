
myList = list(map(int, input().split()))

for i in range(len(myList)):
    if myList.count(myList[i]) == 1:
        print(myList[i], end=' ')
