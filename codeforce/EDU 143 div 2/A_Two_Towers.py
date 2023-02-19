from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a,b=map(int,input().split())
    c=list(map(str,input()))
    d=list(map(str,input()))
    f=0
    e=c+d[::-1]
    for i,j in zip(e,e[1:]):
        if i==j:
            f+=1
    if f>1:
        print("NO")
    else:
        print("YES")