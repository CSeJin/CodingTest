# 방법 1
def solution(number, n, m):
    return 1 if (number%n==0)&(number%m==0) else 0

# 방법 2
def solution(number, n, m):
    return int((number%n==0)&(number%m==0))