from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    d=list(map(int,input().split()))
    c.sort()
    for i in d:
        f=0
        for j,k in enumerate(c):
            if i>c[j]:
                c[j]=i
                f=1
                break
        if f:
            f=0
        else:
            c[0]=i
        c.sort()
    print(sum(c))