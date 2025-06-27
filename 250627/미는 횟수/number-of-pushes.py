A=input()
B=input()
cnt=0
while True:
    if cnt>len(A):
        print("-1")
        break
    elif A!=B:
        A=A[-1]+A[:-1]
        cnt+=1
    elif A==B:
        print(cnt)
        break
    