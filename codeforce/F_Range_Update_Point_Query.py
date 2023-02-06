a=int(input())
s1=list(map(int,input().split()))
s=list(map(int,input().split()))
s.sort(reverse=True)
s1.sort()
ans=0
for i,j in zip(s,s1):
    ans+=max(i,j)
print(ans)