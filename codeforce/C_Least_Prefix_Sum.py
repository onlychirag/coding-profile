from sys import stdin
import sys
from collections import Counter
from collections import defaultdict
import heapq
input = lambda: stdin.readline().rstrip()
for l in range(int(input())):
    #a=int(input())
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    ans=0
    if a==1:
        print(0)
        continue
    d=[]
    l=0
    c=c[::-1]
    for i in range(b-1):
        if c[i]>0:
            heapq.heappush(d,c[i])
        l+=c[i]
        
        while l>0:
            ans+=1
            l-=2*heapq.heappop(d)
    d=[]
    
    l=0
    for i in range(b,a):
        if c[i]<0:
            heapq.heappush(d,c[i])
        l+=c[i]
        
        while l<0:
            ans+=1
            l-=2*heapq.heappop(d)
    print(ans)
#    for i in range(b,a):
