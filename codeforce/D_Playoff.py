a=int(input())
b=list(map(int,input()))
a1=a0=0
for i in b:
    if i==0:
        a0+=1
    else:
        a1+=1
l,p=pow(2,a)-pow(2,a0)+1,pow(2,a1)
for i in range(p,l+1):
    print(i,end=" ")
print()
