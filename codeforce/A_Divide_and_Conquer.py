from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a=int(input())
    #a,b=(map(int,input().split()))
    c=list(map(int,input().split()))
    ans=0
    d=[]
    
    flag=1
    lpo=sorted(list(set(c)))
    m=lpo[-2]
    for i,j in enumerate(c):
        
        if j==m:
            
            continue
        if j>m:
            d.append(i+1,(j//m+1)*m-j)
            ans+=1
        else:
            oi=m//j-1
            d.append(i+1,j,oi)
            ans+=oi
            if m%j:
                d.append(i+1,m%j,1)
                ans+=1
    print(ans)
    for i,j,z in d:
        for mlp in range(z):
            print(i,j)
