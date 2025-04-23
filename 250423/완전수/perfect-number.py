start, end = map(int, input().split())
cnt=0
# Please write your code here.
for i in range(start,end+1):
    hap=0
    for j in range(1,i):
        if i%j==0:
            hap+=j
    if hap==i:
        cnt+=1
print(cnt)

