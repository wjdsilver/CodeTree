def lunar_year(n):
    if n%4==0:
        result=True
        if n%100==0 and n%400!=0:
            result=False
    return result


y = int(input())
if lunar_year(y)==True:
    print("true")
else:
    print("false")
