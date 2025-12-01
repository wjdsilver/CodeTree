n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]
seq = True

while seq:
    exploded = False  
    cnt = 1

    new = numbers[:]

    for i in range(1, n):
        if numbers[i] != 0 and numbers[i] == numbers[i - 1]:
            cnt += 1
        else:
            if cnt >= m:
                exploded = True
                for j in range(i - cnt, i):
                    new[j] = 0
            cnt = 1

    if cnt >= m:
        exploded = True
        for j in range(n - cnt, n):
            new[j] = 0

    numbers = new

    if not exploded:
        seq = False
        break

    newnumbers = [v for v in numbers if v != 0]
    newnumbers += [0] * (n - len(newnumbers))
    numbers = newnumbers

numbers = [v for v in numbers if v != 0]

print(len(numbers))
for elem in numbers:
    print(elem)