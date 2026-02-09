n = int(input())

stack = []
sum= 0

for _ in range(n):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

for i in stack:
    sum += i
print(sum)
