A=input()
ans=A[:2]+A[3:]
ans=ans[:(len(ans)-2)]+ans[len(ans)-1:]
print(ans)