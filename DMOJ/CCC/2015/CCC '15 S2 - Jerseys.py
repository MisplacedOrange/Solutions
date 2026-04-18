import sys


def solve():
    J = int(sys.stdin.readline())
    A = int(sys.stdin.readline())
    sizes = []
    sizes.append(0)
    for i in range(J):
        size = sys.stdin.readline().strip()
        sizes.append(size)
    count = 0

    for j in range(A):
        jsize, zzz = sys.stdin.readline().split()
        jnum = int(zzz)
        if ord(sizes[jnum]) <= ord(jsize):
            count += 1
            sizes[jnum] = "Z"
        else:
            pass
    print(count)
        
solve()