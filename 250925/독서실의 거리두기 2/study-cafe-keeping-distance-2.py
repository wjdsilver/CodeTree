N = int(input())
seats = list(input())
seat_candidate=[0]*N
ans=N
first,last=0,0
temp=0

for i in range(N):
    if seats[i]=="1":
        temp=i
        if seat_candidate[0]=="0":
            first=i
        for j in range(i+1,N):
            if seats[j]=="1":
                seat_candidate[i]=j-i#seat_candidate에 다음 1까지의 거리 저장
                break
    if seat_candidate[N-1]==0:
        last=N-temp-1

if max(max(seat_candidate)//2,first,last)==max(seat_candidate)//2:
    seats[(seat_candidate.index(max(seat_candidate)))+max(seat_candidate)//2]="1"
elif max(max(seat_candidate)//2,first,last)==first:
    seats[0]="1"
elif max(max(seat_candidate)//2,first,last)==last:
    seats[N-1]="1"

for i in range(N):
    if seats[i]=="1":
        for j in range(i+1,N):
            if seats[j]=="1":
                ans=min(ans,j-i)
                break

print(ans)