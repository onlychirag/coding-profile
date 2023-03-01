from sys import stdin
import sys
from collections import Counter
from collections import defaultdict

a=[]
for i in range(1,100):
    if i%3==0:
        a.append("F")
    if i%5==0:
        a.append("B")
print("".join(a))

    
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    #a,b=map(int,input().split())
    n=int(input())
    c=input()
    if c in a:
        print("Yes")
    else:
        print("No")