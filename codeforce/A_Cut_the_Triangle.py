from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a=set()
    b=set()
    f=0
    f1=0
    m=input()
    for i in range(3):
        c,d=map(int,input().split())
        if c in a:
            f=1
        else:
            a.add(c)
        if d in b:
            f1=1
        else:
            b.add(d)
    if f and f1:
        print("NO")
    else:
        print("YES")