
myList = list(map(int, input().split()))
index = int(input())

myList = myList[:index] + myList[index + 1:]

for i in myList:
    print(i, end=' ')
