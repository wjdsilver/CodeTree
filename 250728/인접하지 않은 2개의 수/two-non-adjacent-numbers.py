n = int(input())
numbers = list(map(int, input().split()))
big=0

for i in range(n-2):
    for j in range(i+2,n):
        hap=numbers[i]+numbers[j]
        if big<hap:
            big=hap
print(big)
