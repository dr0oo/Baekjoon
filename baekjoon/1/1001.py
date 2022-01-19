import sys

a, b = map(int, sys.stdin.readline().split())
if a > 0 and b < 10:
    print(a-b)