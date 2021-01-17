
n = int(input())
myList = list(map(int, input().split()))
a = int(input())
num = myList[0]

for i in myList:
    if abs(i - a) < abs(num - a):
        num = i

print(num)
