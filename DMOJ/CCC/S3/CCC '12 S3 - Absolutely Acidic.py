import sys
from collections import Counter

n = int(sys.stdin.readline())
sensors = [int(sys.stdin.readline()) for _ in range(n)]

counter = Counter(sensors).most_common()
mostfreq = counter[0][1]
freqs = []
for value, freq in counter:
    if freq == mostfreq:
        freqs.append(value)
    else:
        break

if len(freqs) > 1:
    print(abs(max(freqs) - min(freqs)))
else:
    winner = freqs[0]
    if len(counter) > 1:
        second_freq = counter[len(freqs)][1]
        runners_up = []
        
        for i in range(len(freqs), len(counter)):
            if counter[i][1] == second_freq:
                runners_up.append(counter[i][0])
            else:
                break
        print(max(abs(winner - max(runners_up)), abs(winner - min(runners_up))))
