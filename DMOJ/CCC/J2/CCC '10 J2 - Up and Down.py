a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

nik_steps = 0 
nik_pos = 0 
by_steps = 0 
by_pos = 0 

while nik_steps != s:
    for i in range(a):
        if nik_steps == s:
            break
        nik_steps += 1
        nik_pos += 1

    for i in range(b):
        if nik_steps == s:
            break
        nik_steps += 1
        nik_pos -= 1

while by_steps != s:
    for i in range(c):
        if by_steps == s:
            break
        by_steps += 1
        by_pos += 1

    for i in range(d):
        if by_steps == s:
            break
        by_steps += 1
        by_pos -= 1
if nik_pos > by_pos:
    print("Nikky")
elif by_pos > nik_pos:
    print("Byron")
else:
    print("Tied")