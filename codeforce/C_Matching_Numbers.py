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
#    c=list(map(int,input().split()))
    b=2*n
    a=n+n//2
    if n%2==0:
        print("NO")
        continue
    else:
        print("YES")
    d=[]
    for i in range(1,n+1):
        if i%2:
            print(i,b)
            d.append(i+b)
            b-=1
        else:
            print(i,a)
            d.append(i+a)
            a-=1
    