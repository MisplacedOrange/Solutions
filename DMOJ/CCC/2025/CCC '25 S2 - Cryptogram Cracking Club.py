import sys

repeat = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
pattern = []


i = 0
# total expanded len 
# Ex. a2b
# = aab
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

# find remainder
index = n % totallen

for char, num in pattern:
    
    # remainder based check
    if index < num:
        print(char)
        break
    # Subtract num from remainder
    else:
        index -= num