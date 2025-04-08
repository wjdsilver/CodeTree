n=int(input())
num=1

for i in range(n): 
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i,0,-1):
        print(num, end=" ")
        if num<9:
            num+=1
        else:
            num=1
    print()