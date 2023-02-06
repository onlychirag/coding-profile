from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a=int(input())
    #a,b=(map(int,input().split()))
    c=list(map(int,input().split()))
    d=min(c)
    e=max(c)
    mi,ma=0,0
    for i in c:
        if i==d:
            mi+=1
        if i==e:
            ma+=1
    print(2*mi*ma)