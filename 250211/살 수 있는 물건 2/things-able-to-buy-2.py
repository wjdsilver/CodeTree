book=3000
mask=1000
pen=500
m=int(input())
if m>=book:
    print("book")
elif book>m>=mask:
    print("mask")
elif mask>m>=pen:
    print("pen")
else:
    print("no")