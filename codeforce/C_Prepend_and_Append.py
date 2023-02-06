from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a=int(input())
    #a,b=(map(int,input().split()))
    c=list(map(str,input()))
    i=0
    j=a-1
    while i<j:
        if c[i]!=c[j]:
            i+=1
            j-=1
        else:
            break
    print(j-i+1)