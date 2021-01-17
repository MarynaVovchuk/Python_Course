
myList = list(map(int, input().split()))

for i in range(len(myList) - 1):
    if (myList[i] > 0 and myList[i + 1] > 0):
        print(myList[i], myList[i + 1])
        break
    elif (myList[i] < 0 and myList[i + 1] < 0):
        print(myList[i], myList[i + 1])
        break
