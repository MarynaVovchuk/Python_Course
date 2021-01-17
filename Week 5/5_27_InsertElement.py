
A = list(map(int, input().split()))
i, a = map(int, input().split())
B = A[i:]
A = A[:i]
A.append(a)
A += B
for i in A:
    print(i, end=' ')
