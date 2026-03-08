# 방법 1
def solution(my_string, target):
    return 1 if target in my_string else 0

# 방법 2
def solution(my_string, target):
    return int(target in my_string)