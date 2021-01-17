
myList = list(map(int, input().split()))
n = int(input())

for i in range(len(myList)):
    if n > myList[i]:
        print(i + 1)
        break
    elif i == len(myList) - 1:
        print(len(myList) + 1)
