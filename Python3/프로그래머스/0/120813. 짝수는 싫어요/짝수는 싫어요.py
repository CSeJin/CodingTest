# 방법 1
def solution(n):
    return [i for i in range(n+1) if i%2!=0]

# 방법 2
def solution(n):
    return [i for i in range(1, n+1, 2)]