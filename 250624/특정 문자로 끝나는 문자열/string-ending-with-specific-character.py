arr=[
    input() for i in range (10)
]

a=input()
ans="N"

for string in arr:
    if string[-1]==a:
        print(string)
        ans="Y"
if ans=="N":
    print("None")