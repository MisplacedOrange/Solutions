n = int(input().strip())

m1 = int(input().strip())
m2 = int(input().strip())
m3 = int(input().strip())

playcount = 0

while n > 0:
    n -= 1
    playcount +=1
    m1 += 1
    if m1 == 35:
        n += 30
        m1 = 0
    if n == 0:
        print(f"Martha plays {playcount} times before going broke.")
        break
    
    n -= 1
    playcount +=1
    m2 += 1
    if m2 == 100:
        n += 60
        m2 = 0
    if n == 0:
        print(f"Martha plays {playcount} times before going broke.")
        break

    n -= 1
    playcount +=1
    m3 += 1
    if m3 == 10:
        n += 9
        m3 = 0
    if n == 0:
        print(f"Martha plays {playcount} times before going broke.")
        break