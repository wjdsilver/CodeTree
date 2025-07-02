def lunar_year(n):
    result=False
    if n%4==0:
        result=True
        if n%100==0 and n%400!=0:
            result=False
    return result
    
    
def month(Y,M,D):
    if M<=12:
        if M in [4,6,9,11]:
            if D>30:
                return False
        elif M in [1,3,5,7,8,10,12]:
            if D>31:
                return False
        elif M==2:
            if lunar_year(Y)==True and D>29:
                return False
            if lunar_year(Y)==False and D>28:
                return False
        else:
            return True
    else:
        return False


def season(M):
    if M in [3,4,5]:
        print("Spring")
    if M in [6,7,8]:
        print("Summer")
    if M in [9,10,11]:
        print("Fall")
    if M in [12,1,2]:
        print("Winter")

        
Y, M, D = map(int, input().split())
if (Y,M,D):
    if month(Y,M,D)==False:
        print("-1")
    else:
        season(M)
        




