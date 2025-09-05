N, M = map(int, input().split())
a = list(map(int, input().split()))

minN=2*sum(a)//M
fin=1000
for x in range(min(a),minN):#구간 합 기준?
    arr=[]
    tmp=0
    for n in a:
        tmp+=n
        if tmp>=x:
            arr.append(tmp)
            tmp=0
        else:
            continue
    if tmp!=0:
        arr.append(tmp)
    if len(arr)==M:
        fin=min(max(arr),fin)
print(fin)
        
