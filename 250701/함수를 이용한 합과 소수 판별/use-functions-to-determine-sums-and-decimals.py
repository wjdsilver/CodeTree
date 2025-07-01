def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


def even(n):
    if (n//100 + n//10 + n%10)%2==0:
        return True
    else:
        return False


a, b = map(int, input().split())
cnt=0
for i in range(a,b+1):
    if prime(i)==True and even(i)==True:
        cnt+=1
print(cnt)