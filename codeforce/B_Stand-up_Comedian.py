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
    #n=int(input())
    #a,b=(map(int,input().split()))
    c=list(map(int,input().split()))
    if c==[0,0,0,0]:
        print(0)
        continue
    if c[0]==0:
        print(1)
        continue
    a=c[0]
    ans=sum(c)
    c[1]+=a
    c[2]+=a
    if 2*min(c[1],c[2])+1<ans:
        print(2*min(c[1],c[2])+1)
    else:
        print(ans)