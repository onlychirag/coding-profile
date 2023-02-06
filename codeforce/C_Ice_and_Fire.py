from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a=int(input())
    #a,b,c=(map(int,input().split()))
    d=list(map(int,input()))
    ans=[1]
    for i in range(1,a-1):
        if d[i]==d[i-1]:
            ans.append(ans[-1])
        else:
            ans.append(i+1)
    print(*ans)