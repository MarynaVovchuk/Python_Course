
myList = list(map(int, input().split()))
minPos = myList[0]

for i in range(len(myList)):
    if minPos <= 0 and myList[i] > 0:
        minPos = myList[i]
    elif myList[i] > 0 and minPos > myList[i]:
        minPos = myList[i]

print(minPos)
