def magic(n):
    result="No"
    if n%2==0 and (n%10+n//10)%5==0:
        result="Yes"
    return result


n = int(input())
print(magic(n))