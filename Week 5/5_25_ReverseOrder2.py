
myList = list(map(int, input().split()))

for i in range(len(myList) // 2):
    myList[i], myList[len(myList) - i - 1] = \
    myList[len(myList) - i - 1], myList[i]

for i in myList:
    print(i, end=' ')
