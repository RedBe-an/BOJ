from math import gcd

A, B = map(int, input().split())
C = 1

h = gcd(C * B - A, B)
print((C * B - A) // h, B // h)
