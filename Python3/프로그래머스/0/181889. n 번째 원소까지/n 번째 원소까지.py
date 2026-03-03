# 방법 1
def solution(num_list, n):
    return [num_list[i] for i in range(n)]

# 방법 2
def solution(num_list, n):
    return num_list[:n]
        