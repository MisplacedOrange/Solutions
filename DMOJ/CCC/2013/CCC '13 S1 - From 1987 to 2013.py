year = int(input())
n = year

while True:
    n += 1
    seen = set(str(n))
    if len(seen) == len(str(n)):
        print(n)
        break
