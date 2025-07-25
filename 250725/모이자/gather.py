import sys

n = int(input())
A = list(map(int, input().split()))
min_d=sys.maxsize

for i in range(n): #i로 만나는 장소
    d=0
    for j in range(n): #각 거리
        d+=A[j]*abs(j-i)
    min_d=min(min_d,d)
print(min_d)

