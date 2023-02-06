from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    ans=0
    c=[]
    j=3
    a1=0
    a2=0
    a0=0
    
    for i in b:
        if i%j==1:
            a1+=1
        if i%j==2:
            a2+=1
        else:
            a0+=1
    ans=0
    o=abs(a2-a1)
    lm=[0,6,5,4,3]
    lp=[0,6,5,4,3]
    if a2==0:
        if a1!=0:
            if a1>4:
                print(((a1//4)*3+a1%4*2))
                continue
            else:
                print(lm[a1])
                continue
        else:
            print(0)
            continue
    if a1==0:
        if a2!=0:
            if a2>4:
                print(((a2//4)*3+a2%4*2))
                continue
            else:
                print(lm[a2])
        else:
            print(0)
            continue
    
    else:
        print((o//4)*3+lp[o%4]+min(a1,a2))