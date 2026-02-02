s, r = map(int, input().split())
print("CIRCLE" if 3.14 * r**2 > s**2 else "SQUARE")