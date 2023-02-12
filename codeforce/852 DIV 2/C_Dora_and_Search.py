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
    a=1
    b=n
    i=0
    j=n-1
    f=0
    while i<j:
        if c[i]==a:
            i+=1
            a+=1
            continue
        if c[i]==b:
            i+=1
            b-=1
            continue
        if c[j]==a:
            j-=1
            a+=1
            continue
        if c[j]==b:
            j-=1
            b-=1
            continue
        else:
            f=1
            break
    if j-i>2:
        print(i+1,j+1)
    else:
        print(-1)