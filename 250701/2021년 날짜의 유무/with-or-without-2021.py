def feb(D):
    if D<=28:
        return True
    else:
        return False


def M30(D):
    if D<=30:
        return True
    else:
        return False


def M31(D):
    if D<=31:
        return True
    else:
        return False


M, D = map(int, input().split())
if M<=12:
    if M==2:
        result=feb(D)
    elif M==4 or M==6 or M==9 or M==11:
        result=M30(D)
    else:
        result=M31(D)
else:
    result=False

if result==True:
    print("Yes")
else:
    print("No")
