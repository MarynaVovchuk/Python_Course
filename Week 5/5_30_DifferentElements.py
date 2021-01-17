
elems = list(map(int, input().split()))
count = 1

for i in range(len(elems) - 1):
    if elems[i] != elems[i + 1]:
        count += 1

print(count)
