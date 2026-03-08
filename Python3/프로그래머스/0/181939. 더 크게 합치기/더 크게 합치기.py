# 방법 1
def solution(a, b):
    ab = int(str(a)+str(b))
    ba = int(str(b)+str(a))
    
    return max(ab, ba)

# 방법 1
def solution(a, b):
    return max(int(f"{a}{b}"), int(f"{b}{a}"))