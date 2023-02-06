from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    #=int(input())
    a,b,c=(map(int,input().split()))
    d=list(map(int,input().split()))
    d.sort()
    if b<c:
        print("NO")
        continue
    for i in range(a%c):
        d[b-i-1]-=1
    d.sort()
    if a//c<d[b-1]:
        print("NO")
        continue
    print("YES")