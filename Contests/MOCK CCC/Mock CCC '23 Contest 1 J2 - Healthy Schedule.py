n = int(input())
m = int(input())

start_time = n
hours = 0

if n == m:
    hours = 24
else:
    while n != m:
        n = (n + 1) % 24
        hours += 1

sleeptime = 8 <= hours <= 10
bedtime = 20 <= start_time <= 23
waketime = 6 <= m <= 9

if sleeptime and bedtime and waketime:
    print("Healthy")
else:
    print("Unhealthy")
