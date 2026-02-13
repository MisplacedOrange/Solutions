import sys

repeat = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
pattern = []


i = 0
totallen = 0
m = len(repeat)

while i < m:
    char = repeat[i]
    i += 1
    digit = ""
    while i < m and repeat[i].isdigit():
        digit += repeat[i]
        i += 1
    num = int(digit)
    pattern.append((char, num))
    totallen += num

index = n % totallen

for char, num in pattern:
    if index < num:
        print(char)
        break
    else:
        index -= num