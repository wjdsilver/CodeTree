n=int(input())
number="N"
for i in range(2,n):
    if n%i==0:
        number="C"
print(number)
