from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    d=list(map(int,input().split()))
    dp=[[-1]*50 for i in range(10**5+1)]
    def s(i,dp1,val,m):
        if i>m:
            return 0
        if dp[i][val+24]!=-1:
            return dp[i][val+24]
        sol=float("-inf")
        if(dp1[i]==0):
            if(val>-24):
                sol=max(sol,s(i+1,dp1,val-1,m))
            if(val<24):
                sol=max(sol,s(i+1,dp1,val+1,m))
        elif(dp1[i]==1):
            if(val>=0):
                if(val<24):
                    sol=max(sol,s(i+1,dp1,val+1,m)+1)
                if(val>1):
                    sol=max(sol,s(i+1,dp1,val-1,m)+1)
            if val<=1:
                sol=max(sol,s(i+1,dp1,0,m))
        else:
            if val<=0:
                if val>=-24:
                    sol=max(sol,s(i+1,dp1,val+1,m)+1)
                if val<=0:
                    sol=max(sol,s(i+1,dp1,val-1,m)+1)
            if val>=-1:
                sol=max(sol,s(i+1,dp1,0,m))
        dp[i][val+24]=sol
        return dp[i][val+24]
    dp1=[0]*(a+1)
    for i,j in zip(c,d):
        dp1[i]=j
    
    print(s(1,dp1,0,a))
    #print(dp[i][24])