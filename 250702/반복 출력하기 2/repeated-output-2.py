n = int(input())

def Hello(n):
    if n == 0: 
        return

    Hello(n - 1)
    print("HelloWorld")


Hello(n)