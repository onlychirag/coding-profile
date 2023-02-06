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
    a=c.count(1)
    b=(a+1)//2
    print(n-a+b)