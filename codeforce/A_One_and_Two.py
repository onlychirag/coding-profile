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
    dp=[]
    a=0
    for i in range(n):
        if c[i]==2:
            a+=1
            dp.append(i+1)
    #print(dp)
    if a%2:
        print(-1)
    else:
        if a==0:
            print(1)
            continue
        print((dp[a//2-1]))