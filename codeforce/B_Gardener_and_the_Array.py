print(bin(19))
print(bin(16))
a=22
b=17
#print(int("10110",2),int("11110",2))
print(bin(a))
print(bin(b))

c=a
d=c&a
while d!=b:
    c+=1
    d&=c
print(c)