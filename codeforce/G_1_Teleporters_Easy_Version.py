from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    #a=int(input())
    a,b=(map(int,input().split()))
    c=list(map(int,input().split()))
    d=[0]*a
    for i in range(a):
        d[i]+=i+1+c[i]
    d.sort()
    an=0
    i=0
    while i<a:
        if b>=d[i]:
            b-=d[i]
        else:
            break
        i+=1
    print(i)