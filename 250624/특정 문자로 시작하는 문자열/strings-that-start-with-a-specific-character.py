n=int(input())

arr=[
    input() for i in range (n)
]

a=input()
cnt=0
ans=0

for string in arr:
    if string[0]==a:
        cnt+=1
        ans+=len(string)
print(f"{cnt} {(ans/cnt):.2f}")