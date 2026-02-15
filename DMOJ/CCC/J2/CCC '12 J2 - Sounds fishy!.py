import sys

depth = [int(sys.stdin.readline()) for _ in range(4)]

rising = True
diving = True
constant = True

for i in range(len(depth) - 1):
    current = depth[i]
    right = depth[i+1]

    if current >= right:
        rising = False
        
    if current <= right:
        diving = False
        
    if current != right:
        constant = False

if constant:
    print("Fish At Constant Depth")
elif rising:
    print("Fish Rising")
elif diving:
    print("Fish Diving")
else:
    print("No Fish")