arr = list(map(int, input().split()))

result = []

for i in arr:
    if i==0:
        break
    if i % 2 == 0:
        result.append(i // 2)
    else:
        result.append(i + 3)
        
print(*result)