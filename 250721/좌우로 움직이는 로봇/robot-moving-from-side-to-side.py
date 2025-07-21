n, m = map(int, input().split())
arr_a=[]
arr_b=[]

pos=0
for _ in range(n):
    t, d = input().split()
    t=int(t)
    for _ in range(t):
        if d == "L":
            pos -= 1
        else:
            pos += 1
        arr_a.append(pos)

pos=0
for _ in range(m):
    t, d = input().split()
    t=int(t)
    for _ in range(t):
        if d == "L":
            pos -= 1
        else:
            pos += 1
        arr_b.append(pos)
        

minT = min(len(arr_a), len(arr_b))
maxT = max(len(arr_a), len(arr_b))
cnt=0

for i in range(1,minT+1):
    if arr_a[i-1] != arr_b[i-1] and arr_a[i] == arr_b[i] :
        cnt+=1
if minT==len(arr_a):
    for j in range(minT+1,maxT-1):
        if arr_a[minT-1]!=arr_b[j-1] and arr_a[minT-1]==arr_b[j] :
            cnt+=1
else:
    for j in range(minT+1,maxT-1):
        if arr_b[minT-1]!=arr_a[j-1] and arr_b[minT-1]==arr_a[j] :
            cnt+=1
print(cnt)