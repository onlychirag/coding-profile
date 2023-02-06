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
    #n=int(input())
    a=list(map(int,input().split()))
    ans=a+a[::-1]
    b=0
    print(ans)
    for i in range(len(ans)-1):
        for j in range(i+1,len(ans)):
            if ans[i]>ans[j]:
                print(ans[i],ans[j])
                b+=1
    print(b)