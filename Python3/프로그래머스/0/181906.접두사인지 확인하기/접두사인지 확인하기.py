# 방법 1
def solution(my_string, is_prefix):
    if len(is_prefix) > len(my_string):
        return 0
    for i in range(len(is_prefix)):
        if my_string[i]!=is_prefix[i]:
            return 0
    return 1

# 방법 2
def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))

# 방법 3
def solution(my_string, is_prefix):
    if my_string[:len(is_prefix)] == is_prefix:
        return 1
    return 0