
myList = list(map(int, input().split()))
count = 0
for i in range(len(myList)):
    count += myList.count(myList.pop())
print(count)
