from itertools import chain
from operator import xor
from sys import stdin
import sys
from collections import Counter
from collections import defaultdict
from functools import reduce
import bisect
import math
import heapq
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    n=int(input())
    #n,a,b=(map(int,input().split()))
    #c=list(map(str,input()))
    dp=[]
    for i in range(n):
        c=list(map(int,input().split()))
        dp.append(c)
    e=float("inf")
    if n%2==0:
        e=n//2
    a1=0
    a2=0
    oi=n//2
    k=1
    d=defaultdict(int)
    ss=set()
    s=set()
    for i in range(1,n+1):
        ss.add(i)
    for i in range(n-1):
        for j in dp:
            d[j[i]]+=1
        e=max(d,key=d.get)
        print(e,end=" ")
        s.add(e)
        d[e]=0
    for i in (ss-s):
        print(i)