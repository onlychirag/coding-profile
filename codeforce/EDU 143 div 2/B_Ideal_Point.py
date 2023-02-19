from sys import stdin
import sys
from collections import Counter,defaultdict
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a,b=map(int,input().split())
    dd=defaultdict(int)
    s=set()
    l,r=0,10**9
    for i in range(a):
        c,d=map(int,input().split())
        if c<=b<=d:
            l=max(c,l)
            r=min(d,r)
    if l==r and l==b:
        print("YES")
    else:
        print("NO")