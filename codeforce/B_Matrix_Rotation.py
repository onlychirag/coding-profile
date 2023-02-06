from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()

for i in range(int(input())):
    #a=int(input())
    a,b=(map(int,input().split()))
    c,d=(map(int,input().split()))
    
    #a,b=min(a,b),max(a,b)
    #c,d=min(c,d),max(c,d)
    if a<b<d and a<c<d:
        print("YES")
        continue
    if a>b>d and a>c>d:
        print("YES")
        continue
    if c<a<b and c<d<b:
        print("YES")
        continue
    if c>a>b and c>d>b:
        print("YES")
        continue
    else:
        print("NO")