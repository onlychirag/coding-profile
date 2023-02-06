from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a=int(input())
    #a,b=(map(int,input().split()))
    c=list(map(str,input()))
    k,j=0,0
    f=0
    for i in c:
        if i=="R":
            j+=1
        if i=="U":
            k+=1
        if i=="L":
            j-=1
        if i=="D":
            k-=1
        if k==1 and j==1:
            f=1
    if f:
        print("YES")
    else:
        print("NO")
