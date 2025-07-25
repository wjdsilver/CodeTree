import sys
n = int(input()) #방 갯수
a = [int(input()) for _ in range(n)] #방 당 인원수
min_d=sys.maxsize


for i in range(n):#시작을 어디서 할건지
    d=0
    for j in range(n):#각 방 거리
        if i>j:
            d+=a[j]*(n-i+j)
        else:
            d+=a[j]*(j-i)
        #print(i,j,d)
    min_d=min(d,min_d)
print(min_d)
