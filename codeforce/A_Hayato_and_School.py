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
    o=[]
    e=[]
    for i,j in enumerate(c):
        if j%2:
            o.append(i+1)
        else:
            e.append(i+1)
    if n==3:
        if len(o)==2 or len(e)==3:
            print("NO")
            continue
        else:
            print("YES")
            print(*o,*e)
            continue
    else:
        if len(o)==0:
            print("NO")
            continue
        
        print("YES")
        if len(o)==1:
            print(o[0],e[0],e[1])
        elif len(o)>=3:
            print(o[0],o[1],o[2])
        else:
            print(o[0],e[0],e[1])
    