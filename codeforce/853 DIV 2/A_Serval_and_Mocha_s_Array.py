from math import gcd
from sys import stdin
import sys
from collections import Counter

input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    d=1
    f=0
    for i in range(a):
        d=gcd(d,b[i])
    for i in range(a):
        for j in range(i+1):
            if gcd(b[i],b[j])<3:
                f=1
                break
        if f:
            break
    if f:
        print("YES")
    else:
        print("NO")