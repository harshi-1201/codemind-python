a,b,c=map(int,input().split())
s=a*(pow(1+(b/100),c))
print("{:.2f}".format(s))