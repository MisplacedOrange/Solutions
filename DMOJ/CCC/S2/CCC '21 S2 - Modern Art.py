# IMPORTANT
# Fails Batch 6 on DMOJ due to TLE
# Solution is 10/15 points on CCC '21 S2 - Modern Art

import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

canvas = [['B' for _ in range(n)] for _ in range(m)]

for _ in range(k):
    rc, num = sys.stdin.readline().split()
    num = int(num) -1
    if rc == 'C':
        for i in range(m):
            canvas[i][num] = 'G' if canvas[i][num] == 'B' else 'B'
    if rc == 'R':
        for j in range(n):
            canvas[num][j] = 'G' if canvas[num][j] == 'B' else 'B'
count = 0
for m in canvas:
    count += m.count('G')

print(count)
