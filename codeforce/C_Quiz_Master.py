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
    c=list(map(int,input().split()))
    c.sort()
        
    def findlcm(a, b):
        
        if (b == 1):
            return a
        

        a = (a * b)//math.gcd(a, b)
    
        b -= 1
        
        return findlcm(a, b)
    if b<3:
        m=b
    else:
        m=findlcm(b,b-1)
    n=m/c[0]
    print(m)
    for i in range(1,a):
        l=0