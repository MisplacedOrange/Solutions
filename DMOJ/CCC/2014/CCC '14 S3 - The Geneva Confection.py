import sys

input = sys.stdin.read().split()
i = 0

T = int(input[i])
i += 1

for _ in range(T):
    N = int(input[i])
    i += 1
    
    mountain = []
    for _ in range(N):
        mountain.append(int(input[i]))
        i += 1
    
    branch = []
    target = 1
    possible = True
    
    while target <= N:
        
        if mountain and mountain[-1] == target:
            mountain.pop()
            target += 1
        elif branch and branch[-1] == target:
            branch.pop()
            target += 1
        elif mountain:
            branch.append(mountain.pop())
        else:
            possible = False
            break
            
    if possible:
        print("Y")
    else:
        print("N")