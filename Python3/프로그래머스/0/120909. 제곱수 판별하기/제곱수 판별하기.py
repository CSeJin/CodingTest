# 방법 1
def solution(n):
    return 1 if int(n**0.5) == (n**0.5) else 2

# 방법 2
def solution(n):
    return 1 if (n**0.5).is_integer() else 2