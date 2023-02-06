from sys import stdin
import sys
from collections import Counter
from collections import defaultdict
import heapq
input = lambda: stdin.readline().rstrip()
for l in range(int(input())):
    a=int(input())
    dp=[[0]*a for i in range(a)]
    x=0
    b=1
    c=a*a
    for i in range(a):
        for j in range(a):
            if x==0:
                x^=1
                dp[i][j]=b
                b+=1
            else:
                x^=1
                dp[i][j]=c
                c-=1
    x=1
    for i in dp:
        if x==0:
            x^=1
            print(*i[::-1])
        else:
            x^=1
            print(*i)