arr = list(map(int, input().split()))
temp = []

for i in arr:
    if i == 0:
        break
    temp.append(i)

while temp:
    print(temp.pop(), end=" ")

