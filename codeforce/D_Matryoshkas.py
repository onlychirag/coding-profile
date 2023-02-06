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
    c=list(map(int,input().split()))
    dp=[]
    d=defaultdict(int)
    for i in c:
        if d[i]==0:
            dp.append(i)
        d[i]+=1
    dp.sort()
    ans=pre=0
    e=dp[0]-1
    for i in range(len(dp)):
        if e+1!=dp[i]:
            ans+=d[dp[i]]
        elif d[dp[i]]>pre:
            ans+=d[dp[i]]-pre
        pre=d[dp[i]]
        e=dp[i]
    print(ans)