n = int(input())

list = []

for _ in range(n):
    i = int(input())
    list.append(i)

list.sort()
for i in range(n):
    print(list[i])