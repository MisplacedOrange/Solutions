n = int(input())
count = 0
for left in range(0, 6):
    for right in range(0, 6):
        if left < right:
            break
        if left + right == n:
            count += 1
print(count)