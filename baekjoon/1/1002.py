import sys
import math

T = int(sys.stdin.readline())
count = []

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split(' '))
    d = math.sqrt((x2-x1)**2+(y2-y1)**2)
    if d == (r1+r2) or d == abs(r2-r1):
        count.append(1)
    elif d == 0 and r1 == r2:
        count.append(-1)
    else:
        if d > (r1+r2) or d < abs(r2-r1):
            count.append(0)
        elif d < (r1+r2) or d > abs(r2-r1):
            count.append(2)

for cnt in count:
    print(cnt)