n=int(input())
prime="P"

for i in range(2,n):
    if n%i==0:
        prime="C"
        break
print(prime)
