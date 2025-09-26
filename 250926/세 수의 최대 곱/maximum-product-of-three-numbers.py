n = int(input())
arr = sorted(list(map(int, input().split())))
new_arr=[]

ppp=arr[n-1]*arr[n-2]*arr[n-3] #셋다 양수
pnn=arr[0]*arr[1]*arr[n-1] #하나양수 두개 절대값큰음수
nnn=0 #셋다 절대값 작은 음수

if 0 in arr: 
    nnn=0
else:
    for i in range(n):
        if arr[i]<0:
            new_arr.append(arr[i])
    new_arr.sort()
    if len(new_arr)>=3:
        nnn=new_arr[-1]*new_arr[-2]*new_arr[-3]
    elif len(new_arr)==1:
        nnn=new_arr[0]*arr[-1]*arr[-2]

print(max(ppp,pnn,nnn))
