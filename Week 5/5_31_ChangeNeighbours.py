
myList = list(map(int, input().split()))

for i in range(0, len(myList) - 1, 2):
    myList[i], myList[i + 1] = myList[i + 1], myList[i]

for i in myList:
    print(i, end=' ')
