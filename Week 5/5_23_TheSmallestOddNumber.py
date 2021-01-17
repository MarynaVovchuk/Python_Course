
myList = list(map(int, input().split()))
minOdd = myList[0]

for i in myList:
    if i % 2 != 0 and minOdd % 2 == 0:
        minOdd = i
    elif i % 2 != 0 and i < minOdd:
        minOdd = i

print(minOdd)
