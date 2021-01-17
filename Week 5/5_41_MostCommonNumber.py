
myList = list(map(int, input().split()))
max = 0

for i in range(1, len(myList)):
    if myList.count(myList[i]) > myList.count(myList[max]):
        max = i

print(myList[max])
