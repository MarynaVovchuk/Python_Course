
a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
counter = 0

for x in range(1001):
    if(a * x ** 3 + b * x ** 2 + c * x + d) * (x - e) == 0 and x != e:
        counter += 1

print(counter)
