from sys import stdin
import sys
from collections import Counter
from collections import defaultdict


input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    #a,b=map(int,input().split())
    #n=int(input())
    c=list(map(str,input()))
    c.sort()
    ans=""
    an=""
    j=0
    k=0
    for i in range(len(c)):
        if i%2==0:
            ans+=c[i]
        
        else:
            an=c[i]+an
            
        
    print(an[::-1]+ans[::-1])