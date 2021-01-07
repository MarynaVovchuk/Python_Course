
def IsPointInCircle(x, y, xc, yc, r):
    return pow(x - xc, 2) + pow(y - yc, 2) <= pow(r, 2)

x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())

if IsPointInCircle(x, y, xc, yc, r):
    print("YES")
else:
    print("NO")
