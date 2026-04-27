N, D = map(int, input().split())
bombs = list(map(int, input().split()))

max_setoff = 1
max_chain = 1
best_chain = 0

for i in range(len(bombs) - 1):
    if abs(bombs[i] - bombs[i + 1]) <= D:
        pass
    else:
        max_setoff += 1

for i in range(len(bombs) - 1):
    if abs(bombs[i] - bombs[i + 1]) <= D:
        max_chain += 1
    else:
        best_chain = max(best_chain, max_chain)
        max_chain = 1
best_chain = max(best_chain, max_chain)
 
print(max_setoff)
print(best_chain)


# 10 - 7 = 3 <= 3 # 2
# 7 - 5 = 3 <= 3 # 3
# 5 - 9 = 4 <= 3 # 4 X
# 9 - 1 = 8 <= 3 # 5 X
# 1 - 1 = 0 <= 3 # 6
# 1 - 7 = 6 <= 3 # 7 X
# 7 - 10 = 3 <- 3 # 8

# 
