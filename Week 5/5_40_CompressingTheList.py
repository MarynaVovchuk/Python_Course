
myList = list(map(int, input().split()))
i = len(myList) - 1
while i > -1:
    if myList[i] == 0:
        myList.append(myList.pop(i))
        i += 1
    i -= 1

print(*myList)
