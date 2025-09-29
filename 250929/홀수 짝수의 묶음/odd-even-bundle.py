N = int(input())
numbers = list(map(int, input().split()))
even,odd=0,0
ans=0

for i in range(N):
    if numbers[i]%2==0:
        even+=1
    elif numbers[i]%2==1:
        odd+=1

if even==odd or even==odd+1:#짝홀짝홀이거나 짝홀짝
    ans=even+odd
else:
    if min(even,odd)==even:#홀수가 더 많을때는 합쳐서 짝수를 만들수 있으나
        if (odd-even)%3==0:#짝홀 쌍 만들고 남은 홀수*2 홀수 로 짝홀 만들기
            print(2*even+(odd-even)//3*2)
        elif (odd-even)%3==1:#짝홀 쌍 만들고 남은 홀수*4 홀수 홀수*2로 짝홀짝 만들기
            print(2*even+(odd-even-4)//3*2+1)
        elif (odd-even)%3==2:#짝홀 쌍 만들고 남은 홀수*2 홀수 홀수*2로 짝홀짝 만들기
            print(2*even+(odd-even-2)//3*2+1)

    else:#짝수가 더 많을때는 합쳐서 홀수를 만들수 없음.
        print(2*odd+1)
    