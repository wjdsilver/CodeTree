n,num=input().split()
num=int(num)
arr = list(map(int, input().split()))
for _ in range (num):
    arr1 = list(map(int, input().split()))
    q=int(arr1[0])
    i=int(arr1[1])
    if q==1:
        print (arr[i-1])
    elif q==2:
        if i in arr:
            print(arr.index(i)+1)
        elif i not in arr:
            print(0)
    elif q==3:
        e=int(arr1[2])
        for m in range (i-1,e):
            print(arr[m],end=" ")
        print()
        
        

