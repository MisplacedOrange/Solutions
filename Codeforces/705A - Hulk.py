import sys

n = int(sys.stdin.readline())
feeling = ""

for i in range(1, n+1):
    if i % 2 == 0:
        feeling += ("I love ")
    else:
        feeling += ("I hate ")
    if n == i:
        feeling += ("it")
    else:
        feeling += ("that ")
print(feeling)