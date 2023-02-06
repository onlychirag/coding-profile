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
    s=2*n
    a=b=0
    f=0
    for i in range(29):
        ni=(n&(1<<i))
        nni=((n//2)&(1<<i))
        if ni==0 and nni>0:
            a=((1<<i)|a)
            b=((1<<i)|b)
        elif ni>0 and nni==0:
            a=((1<<i)|a)
        elif ni!=0 and nni!=0:
            break
    if a+b==2*(a^b):
        if a==0 and b==0:
            print(-1)
            continue
        print(a,b)
    else:
        print(-1)