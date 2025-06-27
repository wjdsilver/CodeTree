word1=input()
word2=input()
A=""
B=""
for i in word1:
    if ord("0")<=ord(i)<=ord("9"):
        A+=i
    else:
        continue
for i in word2:
    if ord("0")<=ord(i)<=ord("9"):
        B+=i
    else:
        continue
A=int(A)
B=int(B)
print(A+B)