import sys

word = sys.stdin.readline().strip()

uppercount = 0
lowercount = 0

for i in word:

    if i.isupper():
        uppercount += 1
    else:
        lowercount += 1

if uppercount > lowercount:
    print(word.upper())
else:
    print(word.lower())
