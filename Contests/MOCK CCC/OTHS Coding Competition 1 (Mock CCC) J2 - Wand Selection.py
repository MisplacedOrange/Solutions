import math
n = int(input())
mean = 0

explosions = []

for _ in range(n):
    explosions.append(int(input()))

explosions.remove(max(explosions))
for i in explosions:
    mean += i

print(math.floor(mean/len(explosions)))