a,b=input().split()
for i in range(len(a)):
    if ord("0")<=ord(a[i])<=ord("9"):
        continue
    else:
        A=int(a[0:i])
        break
for i in range(len(b)):
    if ord("0")<=ord(b[i])<=ord("9"):
        continue
    else:
        B=int(b[0:i])
        break
print(A+B)