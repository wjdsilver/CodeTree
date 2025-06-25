A=input()
ans=A[:1]+A[2:]
ans=ans[:(len(ans)-2)]+ans[(len(ans)-1):]
print(ans)