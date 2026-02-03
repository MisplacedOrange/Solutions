n = int(input())

xcoords = []
ycoords = []

for _ in range(n):
    x, y = map(int, input().split(','))
    xcoords.append(x)
    ycoords.append(y)

xcoords.sort()
ycoords.sort()


print(f"{xcoords[0] - 1},{ycoords[0] - 1}")
print(f"{xcoords[len(xcoords) - 1] + 1},{ycoords[len(ycoords) - 1] + 1}")