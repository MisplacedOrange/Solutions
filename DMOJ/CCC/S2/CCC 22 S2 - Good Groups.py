import sys

n = int(sys.stdin.readline())
constraint = []
if n == 0:
    pass
else: 
    for _ in range(n):
        pair = sys.stdin.readline().split()
        constraint.append(pair)

m = int(sys.stdin.readline())
constraint2 = []
if m == 0:
    pass
else: 
    for _ in range(m):
        pair = sys.stdin.readline().split()
        constraint2.append(pair)

l = int(sys.stdin.readline())
group = {}
count = 0

for i in range(l):
    char_group = sys.stdin.readline().split()
    for char in char_group:
        group[char] = i

for con1, con2 in constraint:
    if group[con1] != group[con2]:
        count += 1
        
for con1, con2 in constraint2:
    if group[con1] == group[con2]:
        count += 1

print(count)


