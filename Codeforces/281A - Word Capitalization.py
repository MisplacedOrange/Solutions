import sys

word = sys.stdin.readline()
firstletter = word[0].upper()

print(f"{firstletter}{word[1:]}")
