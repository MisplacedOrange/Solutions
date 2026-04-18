n = int(input())
body = ""

for _ in range(n):
    s = input()
    body += s

scount = body.count('s')
Scount = body.count('S')

tcount = body.count('t')
Tcount = body.count('T')

stotal = scount + Scount
ttotal = tcount + Tcount

if stotal > ttotal:
    print("French")
elif ttotal > stotal:
    print("English")
else:
    print("French")