# 방법 1
def solution(n):
    return sum(int(i) for i in str(n))

# 방법 2
def solution(n):
    return sum(map(int, str(n)))