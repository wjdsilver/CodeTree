#####################################
a,b=map(int, input().split())
arr_a=list(map(int, input().split()))
arr_b=list(map(int, input().split()))
result='No'

for i in range(a - b + 1):  # 슬라이딩 윈도우 시작점
    if arr_a[i:i + b] == arr_b:
        result = 'Yes'
        break

print(result)

