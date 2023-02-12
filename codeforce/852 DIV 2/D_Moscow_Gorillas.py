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
#for _ in range(int(input())):
n=int(input())
#a,b=(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))
ans=0
for i in range(n):
    c1=[0]*(n+1)
    d1=[0]*(n+1)
    for j in range(i,n):
        c1[c[j]-1]=1
        d1[d[j]-1]=1
        for z,k in zip(c1,d1):
            if z==k==0:
                ans+=1
                break
            if z!=k:
                break
print(ans)