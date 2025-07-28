n = int(input())
arr = [int(input()) for _ in range(n)]
fin=-1
ans=0

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            a=arr[i]
            b=arr[j]
            c=arr[k]
            ans=a+b+c
            notcarry=True
            while a+b>=10 or b+c>=10 or c+a>=10:
                if a%10+b%10+c%10>=10:
                    notcarry=False
                    break
                a//=10
                b//=10
                c//=10
                
            if notcarry:
                fin=max(fin,ans)
print(fin)
                

            