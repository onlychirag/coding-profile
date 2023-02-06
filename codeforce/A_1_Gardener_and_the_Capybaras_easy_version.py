from sys import stdin
import sys
from collections import Counter
from collections import defaultdict
import heapq
input = lambda: stdin.readline().rstrip()
for l in range(int(input())):
    #a=(input())
    #a,b=map(int,input().split())
    b=input()
    c=list(map(str,b))
    a=c[0]
    d=c[1]
    if c[0]=="a" and c[1]=="b":
        d=b[1:-1]
        f=b[-1]
    else:
        f=b[2:]
    print(a,d,f)