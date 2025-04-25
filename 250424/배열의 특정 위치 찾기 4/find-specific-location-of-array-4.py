arr = list(map(int, input().split()))
temp = []
cnt=0
sum_val=0

for i in arr:
    if i == 0:
        break
    temp.append(i)
for j in temp:
    if j%2==0:
        cnt+=1
        sum_val+=j
print(f"{cnt} {sum_val}")
