import sys

# DSU
def find(i, parent):
    root = i
    while parent[root] != root:
        root = parent[root]
    curr = i
    while parent[curr] != root:
        node = parent[curr]
        parent[curr] = root
        curr = node
    return root

def solve():
    G =  int(sys.stdin.readline().strip())
    P = int(sys.stdin.readline().strip())

    parent = list(range(G + 1))
    
    count = 0

    for _ in range(P):
        planes = int(sys.stdin.readline())
        
        gate = find(planes, parent)

        if gate == 0:
            break
        parent[gate] = gate - 1
        count += 1
    print(count)
solve()




