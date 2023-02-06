from itertools import chain
from operator import xor
from sys import stdin
import sys
from collections import Counter
from collections import defaultdict
from functools import reduce
import bisect
import heapq
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    n=int(input())
    a=list(map(str,input()))
    d={}
    for i in range(26):
        d[i]=[0,chr(i+ord("a"))]
    for i in a:
        d[ord(i)-ord("a")][0]+=1
    #print(d)
    print(d)
    d.sort(key=values)
    #print(d)
    print(d[0])