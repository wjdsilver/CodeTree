arr=input().split()
p1_ill=arr[0]
p1_temp=int(arr[1])

arr=input().split()
p2_ill=arr[0]
p2_temp=int(arr[1])

arr=input().split()
p3_ill=arr[0]
p3_temp=int(arr[1])

if p1_ill=="Y" and p1_temp>=37:
    if (p2_ill=="Y" and p2_temp>=37) or(p3_ill=="Y" and p3_temp>=37):
        print("E")
else:
    if (p2_ill=="Y" and p2_temp>=37) and (p3_ill=="Y" and p3_temp>=37):
        print("E")
    else:
        print("N")