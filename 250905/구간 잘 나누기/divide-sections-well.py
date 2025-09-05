N, M = map(int, input().split()) 
a = list(map(int, input().split()))  
fin=100000

for x in range(min(a),sum(a)+1):#구간 합 기준? 
    arr=[] 
    tmp=0 
    for n in a: 
        if tmp+n>x: 
            arr.append(tmp) 
            tmp=n 
        else: 
            tmp+=n
    if tmp!=0:
        arr.append(tmp) 
    if len(arr)<=M:
        fin=min(max(arr),fin)
print(fin)