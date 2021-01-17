
n = int(input())
sum = 0
allSum = 0

for i in range(1, n):
    a = int(input())
    allSum += i
    sum += a
allSum += n

print(allSum - sum)
