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
    #a,b=(map(int,input().split()))
    c=list(map(int,input().split()))
    l=0
    r=n-1
    ans=(n+1)//2
    mid=ans
    a=n//2
    b=n//2+1+n%2
    d=defaultdict(int)
    for i in range(n):
        d[c[i]]=i
    currs=curre=1
    val = max(mid - min(mid, curre) + currs - 1, (n - max(mid, curre)))
    ans=min(ans,val)
    for i in range(2,n+1):
        if d[i]>d[curre]:
            curre+=1
        else:
            curre=i

            currs=i
        val = max(mid - min(mid, curre) + currs - 1, (n - max(mid, curre)))
        ans=min(ans,val)
    print(ans)