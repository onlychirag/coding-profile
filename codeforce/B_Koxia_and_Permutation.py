from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a,b=map(int,input().split())
    ans=[0]*a
    j=1
    k=a
    c=a-a%2
    for i in range(0,c,2):
        ans[i+1]=j
        j+=1
        ans[i]=k
        k-=1
    if a%2:
        ans[-1]=a//2+1
    print(*ans)
    
        