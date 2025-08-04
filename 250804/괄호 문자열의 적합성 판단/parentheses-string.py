str = input()


def solution(str):
    s = empty stack
    for i in range(str.size):
        if str[i] == '(' :
            s.push('(')
            
    else:
        if s.empty() == true:
            return false
        s.pop()

    if s.empty() == false:
        return false
    return true
