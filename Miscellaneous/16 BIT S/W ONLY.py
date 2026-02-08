n = int(input())

for _ in range(n):
    a, b, c = map(int, input().split())
    if a * b == c:
        print("POSSIBLE DOUBLE SIGMA")
    else: 
        print("16 BIT S/W ONLY")