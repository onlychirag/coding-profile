from sys import stdin
import sys
from collections import Counter
from collections import defaultdict
import heapq
input = lambda: stdin.readline().rstrip()
for l in range(int(input())):
    a=int(input())
    #a,b=map(int,input().split())
    c=list(map(int,input().split()))
    if len(set(c))==1:
        print("NO")
        continue
    print("YES")
    d=Counter(c)
    e=list(set(c))
    e.sort(reverse=True)
    for i in d:
        while d[i]!=1:
            e.append(i)
            d[i]-=1
    print(*e)