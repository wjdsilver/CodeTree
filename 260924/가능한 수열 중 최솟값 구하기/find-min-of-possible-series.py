n = int(input())

def check_seq(seq):
    for i in range(1, len(seq)//2 + 1):
        for j in range(len(seq) - 2*i + 1):
            if seq[j:j+i] == seq[j+i:j+2*i]:
                return False

    return True
            

def make_seq(seq):
    if len(seq)==n:#길이가 N인 가능 수열 만들어지면 수열 리턴  
        return seq
    for i in range(4,7):
        seq.append(i)
        if check_seq(seq) is True:
            result = make_seq(seq)
            if result is not None:
                return result
        seq.pop()
ans=make_seq([])
for i in ans:
    print(i,end="")

