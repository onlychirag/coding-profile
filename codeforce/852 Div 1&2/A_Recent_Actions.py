from sys import stdin
import sys
from collections import Counter
from collections import defaultdict

input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    s=set()
    an=[-1]*(a+1)
    j=a
    for i in range(b):
        if j<0:
            break
        d=len(s)    
        s.add(c[i])
        if  d!=len(s):
            an[j]=str(i+1)
            j-=1
    print(*an[1:])
    #" ".join(an[1:])