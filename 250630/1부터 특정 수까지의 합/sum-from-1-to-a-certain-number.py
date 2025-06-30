def hap(n):
    hap=0
    for i in range(n+1):
        hap+=i
    return hap


n = int(input())
print(hap(n)//10)

