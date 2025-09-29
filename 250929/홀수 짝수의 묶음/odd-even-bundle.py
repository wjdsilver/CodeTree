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
        if (odd-even)%3==0:
            print(2*even+(odd-even)//3*2)
        elif (odd-even)%3==1:
            print(2*even+(odd-even-4)//3*2+1)
        elif (odd-even)%3==2:
            print(2*even+(odd-even-2)//3*2+1)

    else:#짝수가 더 많을때는 합쳐서 홀수를 만들수 없음.
        print(2*odd+1)
    