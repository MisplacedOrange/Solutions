n = int(input())

Antonia = 100
David = 100

for _ in range(n):
    x, y = map(int, input().split())
    if x > y:
        David -= x
    elif y > x:
        Antonia -= y
    else:
        pass

print(Antonia)
print(David)