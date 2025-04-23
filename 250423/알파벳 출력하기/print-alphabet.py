n=int(input())
num=65
for i in range(1,n+1):
    for j in range(i):
        print(chr(num),end="")
        if num==90:
            num=65
        else:
            num+=1
    print()
