from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    n=int(input())
    #a,b=(map(int,input().split()))
    #c=list(map(int,input().split()))
    a=1
    b=0
    a1=0
    b1=2
    n-=1
    m=0
    nn=0
    while n:
        d=min(n,2*b1+1)
        if a1%2==0:
            b+=d//2
            m+=d//2+d%2
        else:
            a+=d//2+d%2
            nn+=d//2
        n-=d
        b1+=2
        a1+=1
    print(a,nn,b,m)
    #print(a//2+m+a%2,a//2-m,b//2+nn+b%2,b//2-nn)