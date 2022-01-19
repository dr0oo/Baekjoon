import sys

a, b = map(int, sys.stdin.readline().split())
if a > 0 and b < 10:
    print(a+b)

#input()으로 받는 것 보다는 stdin.readlin()이 더 효율적임


#이렇게 해도 맞긴 하다 
'''
a, b = map(int, input('').split())
print(a+b)
'''