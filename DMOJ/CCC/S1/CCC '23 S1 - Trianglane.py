import sys

n = int(sys.stdin.readline().strip())
row1 = list(map(int, sys.stdin.readline().split()))
row2 = list(map(int, sys.stdin.readline().split()))

count = 0


for i in range(n):
    if row1[i] == 1:
        count += 3
    if row2[i] == 1:
        count += 3
for i in range(n - 1):
    if row1[i] == 1 and row1[i + 1] == 1:
        count -= 2
    if row2[i] == 1 and row2[i + 1] == 1:
        count -= 2
for i in range(0, n, 2):
    if row1[i] == 1 and row2[i] == 1:
        count -= 2
print(count)


