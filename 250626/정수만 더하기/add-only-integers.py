word=input()
ans=0
for i in range(len(word)):
    if ord("0")<=ord(word[i])<=ord("9"):
        ans=ans+ord(word[i])-ord("0")
    else:
        continue
print(ans)