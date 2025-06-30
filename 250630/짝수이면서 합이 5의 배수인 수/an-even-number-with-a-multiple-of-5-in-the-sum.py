n = int(input())
result="No"

def magic(n):
    if n%2==0 and (n%10+n//10)%5==0:
        result="Yes"
    return result


print(magic(n))