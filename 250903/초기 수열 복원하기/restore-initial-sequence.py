n = int(input())
arr = list(map(int, input().split()))
for x in range(1,arr[0]):#첫번째 숫자 x면
    num1=x
    num2=arr[0]-x
    new_arr = [num1, num2]
    valid = True
    for i in range(1, n-1):
        num_next = arr[i] - new_arr[-1]
        if num_next <= 0 or num_next > n:  # 범위 체크
            valid = False
            break
        new_arr.append(num_next)
    
    if not valid:
        continue

    if sorted(new_arr) == list(range(1, n+1)):
        for elem in new_arr:
            print(elem,end=" ")
        break

