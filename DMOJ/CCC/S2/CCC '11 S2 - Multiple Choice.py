n = int(input())

mcq = [input() for _ in range(n)]
answer = [input() for _ in range(n)]

correct = 0

for i in range(n):
    if mcq[i] == answer[i]:
        correct +=1

print(correct)