import sys
maxweight = int(sys.stdin.readline())
numofcars = int(sys.stdin.readline())
stack = [int(sys.stdin.readline()) for _ in range(numofcars)]

totalweight = 0
totalcars = 0

for i in range(len(stack)):
    totalweight += stack[i] 
    if i >= 4:
        totalweight -= stack[i-4]
    if totalweight > maxweight:
        break
    totalcars += 1
print(totalcars)