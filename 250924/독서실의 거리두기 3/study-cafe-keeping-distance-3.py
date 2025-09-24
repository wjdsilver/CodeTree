N = int(input())
seats = list(input())
seat_candidate=[0]*N
ans=N
for i in range(N):
    if seats[i]=="1":
        for j in range(i+1,N):
            if seats[j]=="1":
                seat_candidate[i]=j-i#seat_candidate에 다음 1까지의 거리 저장
                break

seats[(seat_candidate.index(max(seat_candidate)))+max(seat_candidate)//2]="1"

for i in range(N):
    if seats[i]=="1":
        for j in range(i+1,N):
            if seats[j]=="1":
                ans=min(ans,j-i)
                break
print(ans)

