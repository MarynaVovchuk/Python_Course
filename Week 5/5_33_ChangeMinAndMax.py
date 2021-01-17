
elems = list(map(int, input().split()))
min = elems[0]
max = elems[0]
minI = 0
maxI = 0

for i in range(len(elems)):
    if elems[i] > max:
        max = elems[i]
        maxI = i
    elif elems[i] < min:
        min = elems[i]
        minI = i

elems[minI], elems[maxI] = elems[maxI], elems[minI]
print(*elems)
