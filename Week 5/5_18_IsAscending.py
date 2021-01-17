
def IsAscending(A):
    i = 1
    ok = True
    while i < len(A):
        if A[i - 1] >= A[i]:
            ok = False
        i += 1
    if ok:
        return 'YES'
    else:
        return 'NO'

myList = list(map(int, input().split()))
print(IsAscending(myList))
