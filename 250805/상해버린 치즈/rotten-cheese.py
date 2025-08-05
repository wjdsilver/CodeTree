N, M, D, S = map(int, input().split())
ans=0

eat=[]
for _ in range(D):
    person, cheese, time = map(int, input().split())
    eat.append((person, cheese, time))

sick= []
for _ in range(S):
    person, time = map(int, input().split())
    sick.append((person, time))

for i in range(1,M+1):
    log=[]
    for person, c, time in eat:
        if c == i:
            log.append((person, time))

    possible = True
    for sp, st in sick:
        found = False
        for ep, et in log:
            if sp == ep and et < st:
                found = True
                break
        if not found:
            possible = False
            break

    if possible:
        people = set()
        for person, c, time in eat:
            if c == i:
                people.add(person)
        ans = max(ans, len(people))
print(ans)

