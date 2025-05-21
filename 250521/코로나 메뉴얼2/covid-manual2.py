count_arr = [0] * 4

for i in range (3):
    a,b=input().split()
    b=int(b)
    if a == "Y" and b>=37:
        count_arr[0] += 1
    elif a == "N" and b>=37:
        count_arr[1] += 1
    elif a == "Y" and b<37:
        count_arr[2] += 1
    elif a == "N" and b<37:
        count_arr[3] += 1

for i in range(4):
    print(count_arr[i],end=" ")
if count_arr[0]>=2:
    print("E")



