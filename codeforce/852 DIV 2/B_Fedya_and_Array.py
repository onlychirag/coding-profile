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
    a,b=(map(int,input().split()))
#    c=list(map(int,input().split()))
    a,b=max(a,b),min(a,b)


    p=a
    f=0
    print(2*(abs(a-b)))
    while p>b:
        print(p,end=" ")
        p-=1
    while p<a:
        print(p,end=" ")
        p+=1
    print()