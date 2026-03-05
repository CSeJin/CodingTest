# 방법 1
def solution(n, control):
    dict = {'w':1, 's':-1, 'd':10, 'a':-10}
    for c in control:
        n += dict[c]
    return n

# 방법 2
def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum(key[c] for c in control)