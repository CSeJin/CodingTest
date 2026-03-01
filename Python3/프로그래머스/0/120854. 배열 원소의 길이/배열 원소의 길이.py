# 방법 1
def solution(strlist):
    return [len(s) for s in strlist]

# 방법 2
def solution(strlist):
    return list(map(len, strlist))