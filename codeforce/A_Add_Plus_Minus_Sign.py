from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a=int(input())
    #a,b=(map(int,input().split()))
    c=list(map(int,input()))
    x=c[0]
    ans=""
    for i in c[1:]:
        if i==1:
            if x:
                x^=1
                ans+="-"
            else:
                x^=1
                ans+="+"
        else:
            ans+="+"
    print(ans)