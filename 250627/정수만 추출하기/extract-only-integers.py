a,b=input().split()
A=""
B=""
for i in a:
    if ord("0")<=ord(i)<=ord("9"):
        A+=i
    else:
        break
for i in b:
    if ord("0")<=ord(i)<=ord("9"):
        B+=i
    else:
        break
A=int(A)
B=int(B)
print(A+B)