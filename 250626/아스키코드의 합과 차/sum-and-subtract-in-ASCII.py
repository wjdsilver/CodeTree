a,b=input().split()
aasc=ord(a)
basc=ord(b)
dif=0
if aasc>basc:
    dif=aasc-basc
else:
    dif=basc-aasc
print(aasc+basc, dif)