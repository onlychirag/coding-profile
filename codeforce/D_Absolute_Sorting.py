from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a=int(input())
#    a,b=(map(int,input().split()))
    c=list(map(int,input().split()))
    ans=0
    if sorted(c)==c:
        print(0)
        continue
    if sorted(c)==c[::-1]:
        print(max(c)+1)
        continue
    for i in range(a-1):
        if c[i+1]<c[i]:
            ans=max(ans,(c[i+1]+c[i]+1)//2)
    #print(ans+sum(c))
    #print(ans)
    #continue
    #print(c)
    for i in range(a):
        c[i]=abs(c[i]-ans)
    if sorted(c)==c:
        print(ans)
    else:
        print(-1)