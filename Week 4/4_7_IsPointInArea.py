
def IsPointInArea(x, y):
    y1 = 2 * x + 2
    y2 = -x
    c = (x + 1) ** 2 + (y - 1) ** 2
    return y1 <= y and y2 <= y and c <= 4 or y2 >= y and y1 >= y and c >= 4

x = float(input())
y = float(input())

if IsPointInArea(x, y):
    print("YES")
else:
    print("NO")
