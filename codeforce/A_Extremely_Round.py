
from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    b=int(input())
    a=str(input())
    c=set()
    #a,b=(map(int,input().split()))
    #c=list(map(int,input().split()))
    d=""
    flag=0
    for i in range(b-1):
        if a[i:i+2] in c:
            flag=1
            break 
        e=d
        d=a[i:i+2]
        print(d)
        c.add(d)
    if flag:
        print("NO")
    else:
        print("YES")