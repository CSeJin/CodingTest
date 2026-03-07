# 방법 1
def solution(num_list):
    num = -1
    for n in num_list:
        if n < 0:
            num = num_list.index(n)
            break
    return num

# 방법 1
def solution(num_list):
    for idx, num in enumerate(num_list):
        if num < 0:
            return idx
    return -1