N = int(input())
str = input()
ans=0

for i in range(N):#i길이의 문자열
    s=False
    for j in range(N):#j부터 시작
        sub=str[j:j+i+1] 
        if str[j+1:].count(sub)>=1:
            s=True
            ans=i+2
            break
    if s==False:
        break
print(ans)
