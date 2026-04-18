import sys

n = int(sys.stdin.readline())

streams = [int(sys.stdin.readline()) for _ in range(n)]

while True:
    command = int(sys.stdin.readline())

    if command == 77:
        break

    if command == 99:

        m = int(sys.stdin.readline()) - 1
        percentage = int(sys.stdin.readline()) 

        flow = streams[m]
        left_flow = flow * (percentage/100)
        right_flow = flow - left_flow

        streams[m] = left_flow
        streams.insert(m + 1, right_flow)

    elif command == 88: # join
        m = int(sys.stdin.readline()) - 1
        streams[m] += streams[m + 1]
        streams.pop(m + 1)
        
for i in range(len(streams)):
    print(int(round(streams[i])), end=" ")
    