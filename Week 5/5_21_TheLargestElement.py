
myList = list(map(int, input().split()))
max = myList[0]
maxIndex = 0

for i in range(len(myList)):
    if myList[i] > max:
        max = myList[i]
        maxIndex = i

print(max, maxIndex)
