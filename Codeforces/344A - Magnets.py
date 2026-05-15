import sys
n = int(sys.stdin.readline().strip())

magnet1 = sys.stdin.readline().strip()
count = 1

for i in range(n - 1):
    magnet2 = sys.stdin.readline().strip()
    if magnet2 != magnet1:
        count += 1
        magnet1 = magnet2


print(count)
    