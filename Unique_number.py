n=int(input())
s=[]
k=str(n)
h=len(k)
for i in k:
    if  i not in s:
        s.append(i)
if h==len(s):
    print("Unique Number")
else:
    print("Not Unique Number")