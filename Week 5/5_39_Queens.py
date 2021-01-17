
queens = []

for i in range(8):
    queens.append(list(map(int, input().split())))

ok = False
for i in range(len(queens)):
    for j in range(i + 1, len(queens)):
        if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or \
           abs(queens[i][0] - queens[j][0]) == \
           abs(queens[i][1] - queens[j][1]):
            ok = True
            break

print('YES' if ok else 'NO')
