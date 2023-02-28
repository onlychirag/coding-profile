from sys import stdin
import sys
from collections import Counter
from collections import defaultdict


input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    #a,b=map(int,input().split())
    n=int(input())
    c=list(map(int,input().split()))
    ans=0
    an=[]
    f=0
    if len(set(c))==1:
        print(0)
        continue
    while True:
        if len(set(c))==1:
            break
        mi=min(c)
        ma=max(c)
        i=c.index(ma)
        j=c.index(mi)
        if mi==1:
            f=1
            break
        if ma==mi:
            break
        d=0
        p=ma
        while ma>mi:
            ma=(ma+mi-1)//mi
            d+=1
            if ma==mi:
                
                break

            if ma==p:
                
                break
            
            p=ma
        ans+=d
        an.append([i,j,d])
        c[i]=ma
    if f==1:
        print(-1)
        continue
    print(ans)
    #print(c)
    for i,j,k in an:
        for l in range(k):
            print(i+1,j+1)
