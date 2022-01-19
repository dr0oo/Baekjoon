import sys

a, b = map(int, sys.stdin.readline().split())
if a > 0 and b < 10:
    print(a+b)


#이렇게 해도 맞긴 하다 
'''
a, b = map(int, input('').split())
print(a+b)
'''