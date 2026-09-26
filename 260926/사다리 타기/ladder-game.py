n, m = map(int, input().split()) #n=사람수(세로줄), m=가로줄
edges = [tuple(map(int, input().split())) for _ in range(m)] #가로줄 정보
#엣지를 두번째꺼 기준 정렬->위쪽(우선 순위 높은거)부터 확인 가능
edges.sort(key=lambda x: x[1])

ladder = [0] * n #입력받은대로 했을때의 결과


def get_result(selected):
    result = [0] * n
    for i in range(n):
        curr = i
        for a, b in selected:
            if a == curr + 1: #오른쪽 줄로 이동
                curr += 1
            elif a == curr: #왼쪽 줄로 이동
                curr -= 1
        result[i] = curr

    return result

ladder = get_result(edges)
answer = m

def mincase(idx, selected):
    global answer
    # 이미 현재 답보다 많이 선택했다면 의미 없음
    if len(selected) >= answer:
        return

    # 다 확인했으면
    if idx == m:
        if get_result(selected) == ladder:
            answer = min(len(selected),answer)
        return

    # 선택
    selected.append(edges[idx])
    mincase(idx + 1, selected)
    selected.pop()

    # 선택하지 않음
    mincase(idx + 1, selected)


mincase(0, [])

print(answer)

