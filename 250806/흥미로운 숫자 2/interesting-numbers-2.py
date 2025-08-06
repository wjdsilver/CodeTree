X, Y = map(int, input().split())

cnt = 0
for i in range(X, Y + 1):
    digits = list(set(str(i)))  # 숫자의 각 자리수를 문자로 만든 집합
    if len(digits) == 2:
        if str(i).count(digits[0])*str(i).count(digits[1])==max(str(i).count(digits[0]),str(i).count(digits[1])):
            cnt+=1

print(cnt)

        