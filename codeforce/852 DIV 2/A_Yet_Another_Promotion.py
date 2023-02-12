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
    c,d=(map(int,input().split()))
    if c<=d:
        print(c*min(a,b))
        continue
    if a*(d)<b*(d+1):
        #print(c//(d+1))
        print((c//(d+1))*d*(a)+(c%(d+1))*(min(a,b)))
        continue
    else:
        print(c*b)