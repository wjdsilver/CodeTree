n = int(input())
sequence = []

class Sequence:
    def __init__(self,num,no,afno):
        self.num=num
        self.no=no
        self.afno=0


arr=list(map(int,input().split()))
for i in range(n):
    sequence.append(Sequence(arr[i],i+1,afno=0))
sequence.sort(key=lambda x:x.num)
for i in range(n):
    sequence[i].afno=i+1
sequence.sort(key=lambda x:x.no)
for elem in sequence:
    print(elem.afno,end=" ")