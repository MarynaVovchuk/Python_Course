
myList = list(map(int, input().split()))

myList.insert(0, myList[-1])
myList.pop()

print(*myList)
