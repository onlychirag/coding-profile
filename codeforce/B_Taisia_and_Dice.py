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
    n,a,b=(map(int,input().split()))
    #c=list(map(str,input()))
    print(a-b,end=" ")
    f=b//(n-1)
    g=b%(n-1)
    for i in range(n-1):
        if g:
            g-=1
            print(f+1,end=" ")
        else:
            print(f,end=" ")
    print()