n=int(input())
m=n*n
temp=n
s=0
while m!=0:
    d=m%10
    s=s+d
    m=m//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")