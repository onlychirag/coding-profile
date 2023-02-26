from math import gcd
from sys import stdin
import sys
from collections import Counter

input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a=int(input())
    b=list(map(int,input()))
    i=0
    j=a-1
    an=0
    while i<j:
        if b[i]!=b[j]:
            an+=1
            while i<=j and b[i]!=b[j]:
                i+=1
                j-=1
        i+=1
        j-=1 
    if an>1:
        print("NO")
    else:
        print("YES")
