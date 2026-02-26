# 방법 1
def solution(sides):
    sides.sort()
    longest = sides.pop()
    if longest >= sum(sides):
        return 2
    return 1

# 방법 2
def solution(sides):
    return 1 if max(sides) < (sum(sides)-max(sides)) else 2