n = 2
arr_2d = []

ver=[0]*2
hor=[0]*4
total=0

for _ in range(n):
    arr_1d =list(map(int,input().split()))
    arr_2d.append(arr_1d)

for i in range(n):
    for j in range(4):
        ver[i]+=arr_2d[i][j]
        hor[j]+=arr_2d[i][j]
        total+=arr_2d[i][j]
for i in range(n):
    print(f"{ver[i]/4:.1f}",end=" ")
print()
for j in range(4):
    print(f"{hor[j]/2:.1f}",end=" ")
print()
print(f"{total/8:.1f}")
    
    