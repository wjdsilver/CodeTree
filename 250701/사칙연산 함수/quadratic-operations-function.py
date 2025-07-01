a, o, c = input().split()
a = int(a)
c = int(c)

def operation(a,o,c):
    if o=="+":
        print (a,o,c,"=",a+c)
    elif o=="-":
        print (a,o,c,"=",a-c)
    elif o=="*":
        print (a,o,c,"=",a*c)
    elif o=="/":
        print (a,o,c,"=",a//c)
    else:
        print ("False")


operation(a,o,c)