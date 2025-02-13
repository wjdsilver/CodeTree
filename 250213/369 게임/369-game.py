n=int(input())

for i in range(1,n+1):
    #3으로 나눠떨어질때
    if i%3==0:
        print("0",end=" ")
    #100의 자리수가 3,6,9일때
    elif i>=100 and (i//100)%3==0:
        print("0",end=" ")
    #10의 자리수가 3,6,9일때
    elif i>=10 and (i//10)%3==0:
        print("0",end=" ")
    elif i%10==3 or i%10==6 or i%10==9:
        print("0",end=" ")
    else:
        print(i,end=" ")