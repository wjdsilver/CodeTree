N, M, D, S = map(int, input().split())
ans=0

p, m, t = [], [], []

for _ in range(D):
    person, cheese, time = map(int, input().split())
    p.append(person)
    m.append(cheese)
    t.append(time)

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)

for i in range(1,M):
    sick=0
    if sick_t[sick_p.index(p[m.index(i)])]>t[m.index(i)]:
        sick=m.count(i)
    ans=max(ans,sick)
print(ans)

