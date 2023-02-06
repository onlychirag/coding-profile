from sys import stdin
import sys
from collections import Counter
import bisect
input = lambda: stdin.readline().rstrip()
dp=[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
for _ in range(int(input())):
    a=int(input())
#    a,b=(map(int,input().split()))
    c=list(map(int,input().split()))
    ma=max(c)
    mi=min(c)
    if len(set(c))==1:
        print(0)
        continue
    d=bisect.bisect(dp,ma)
    ans=ma
    mi=ans
    for i in range(a):
        ans|=c[i]
        mi&=c[i]
    print(ans-mi)