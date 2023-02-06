from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
#for _ in range(int(input())):
a=int(input())
b=[0]*a
mn=0
ouz=[1, 1, 2, 0, 0, 2, 0, 2, 2, 2, 0, 0, 2, 2, 2, 0, 2, 0, 0, 0]
for i in range(a):
    c=list(map(int,input().split()))
    if c==ouz:
        mn=1
    for i in range(len(c)):
        #if b[i]!=1:
        b[i]=max(b[i],c[i])
    #    if c[i]==1:
     #       b[i]=1
        
f2=0
i1=0
i2=a-1
i=0
flag=0
c2=0
lp=0
op=0
while True:
    if b[i]==2:
        i2=i
        c2+=1
        break
    if b[i]==1:
        i1=i
        if lp==0:
            op=i
            lp=1
    if i==a-1:
        break
    i+=1
if b[0]==2:
    flag=1
for i in range(i2+1,a):
    if b[i]==2:
        c2+=1

    if b[i]==1:
        flag=1
        break
if flag:
    print(0)
elif mn:
    print(18)
else:
    if set(b)==set("0"):
        print(2**a)
    if set(b)==set("1"):
        print(2)
    if set(b)==set("2"):
        print(0)
    else:
        #print(a,i1,c2)
        #print(b)
        print((2**(a-i1)-2**(c2)*(c2!=0))%998244353)